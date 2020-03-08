from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

# para redireccionar a un sitio
from django.urls import reverse_lazy
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
#decoradores para el LoginRequire y PermissionRequired para trabajarlos en funciones
from django.contrib.auth.decorators import  login_required, permission_required
from django.http import HttpResponse
import json
from django.db.models import Sum

from .models import Proveedor, ComprasEnc, ComprasDet
from .forms import ProveedorForm, ComprasEncForm
from bases.views import SinPrivilegios
from inv.models import  Producto

# Create your views here.
class ProveedorView(LoginRequiredMixin, SinPrivilegios, ListView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "cmp.view_proveedor"
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class ProveedorNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    permission_required = "cmp.add_proveedor"
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = ProveedorForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"
    success_message = "Proveedor creado satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProveedorEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    permission_required = "cmp.change_proveedor"
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = ProveedorForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"
    success_message = "Proveedor Actualizado satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Para borrar categoria de la BD, No se recomienda usar esta forma de borrar por que se pierde el historico
@login_required(login_url='/login/') #seguridad para no ingresar por url
@permission_required('cmp.change_proveedor', login_url='bases:sin_privilegios')#seguridad para no ingresar por url sin permiso
def proveedor_inactivar(request, id):
    pro = Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = "cmp/inactivar.html"

    if not pro:
        return HttpResponse('El proveedor no existe '+ str(id))

    # Mostramos el contenido que vamos a eliminar
    if request.method=='GET':
        contexto = {'obj':pro}

    # Cambiamos el estado de True a False al darle al boton eliminar
    if request.method=='POST':
        pro.estado = False
        pro.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor' + str(id) + 'Inactivado')

    return render(request, template_name, contexto)


#----------------------------------------------- VISTAS DE Compras --------------------------------------
class ComprasView(LoginRequiredMixin, SinPrivilegios, ListView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "cmp.view_comprasenc"
    model = ComprasEnc
    template_name = "cmp/compras_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios')
def compras(request, compra_id=None):
    template_name = "cmp/compras.html"
    #Filtramos los productos
    prod = Producto.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    #GET
    if request.method=='GET':
        form_compras = ComprasEncForm
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            #Tomamos la fecha del envabezado
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }

            # Le pasamos el valor al formulario
            form_compras = ComprasEncForm(e)
        else:
            det = None

        #Inicializamos el contexto con lo que vamos a enviar a la plantilla
        contexto = {'productos':prod, 'encabezado':enc, 'detalle':det, 'form_enc': form_compras}

    #POST
    if request.method=='POST':
        #Capturamos los valores
        fecha_compra = request.POST.get("fecha_compra")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = request.POST.get("proveedor")
        sub_total = 0
        descuento = 0
        total = 0

        #Si no se envia compra id no existe el encabezado acabamos de guardar
        if not compra_id:
            #Filtramos el proveedor
            prov=Proveedor.objects.get(pk=proveedor)

            #Creamos el objeto
            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc = request.user
            )
            #Guardamos el encabezado
            if enc:
                enc.save()
                compra_id=enc.id
        # Si compra id se envia el encabezado existe vamos a editar
        else:
            enc=ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra = fecha_compra
                enc.observacion = observacion
                enc.no_factura=no_factura
                enc.fecha_factura=fecha_factura
                enc.um=request.user.id
                enc.save()

        # Si no tiene nada redirijimos
        if not compra_id:
            return redirect("cmp:compras_list")

        #Haceos lo mismo con detalle
        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")

        prod = Producto.objects.get(pk=producto)

        det = ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc = request.user
        )

        if det:
            det.save()

            #calculamos el subtotal
            sub_total = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            #Actualizamos el encabezado al ser de sum djangole agrega __sum
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()

        return redirect("cmp:compras_edit",compra_id=compra_id)


    return render(request, template_name, contexto)


class CompraDetDelete(SinPrivilegios, DeleteView):
    permission_required = "cmp.delete_comprasdet"
    model = ComprasDet
    template_name = "cmp/compras_det_del.html"
    context_object_name = 'obj'

    # Para regresar a la edicion de la compra
    def get_success_url(self):
          compra_id=self.kwargs['compra_id']
          return reverse_lazy('cmp:compras_edit', kwargs={'compra_id': compra_id})
