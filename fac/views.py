from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import  login_required, permission_required
from django.http import HttpResponse

from django.contrib.auth import authenticate

from .models import Cliente, FacturaEnc, FacturaDet
from .forms import ClienteForm
import inv.views as inv
from inv.models import Producto
from bases.views import SinPrivilegios

# Create your views here.
class ClienteView(LoginRequiredMixin, SinPrivilegios, ListView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "fac.view_cliente"
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


# Vistas base para heredar
class VisatBaseCreate(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    context_object_name = 'obj'
    success_message = "Registro Agregado Satisfactoriamente."

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class VisatBaseEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    context_object_name = 'obj'
    success_message = "Registro Actualizado Satisfactoriamente."

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Clases creadas usando la herencia de clases
class ClienteNew(VisatBaseCreate):
    permission_required = "fac.add_cliente"
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    login_url = "bases:login"


class ClienteEdit(VisatBaseEdit):
    permission_required = "fac.change_cliente"
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    login_url = "bases:login"


@login_required(login_url="/login/")
@permission_required("fac.change_cliente",login_url="/login/")
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method=="POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")

    return HttpResponse("FAIL")


#----------------------------------------------- VISTAS DE FACTURAS --------------------------------------
class FacturaView(LoginRequiredMixin, SinPrivilegios, ListView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "fac.view_facturaenc"
    model = FacturaEnc
    template_name = "fac/factura_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


@login_required(login_url='/login/')
@permission_required('fac.change_facturaenc', login_url='bases:sin_privilegios')
def facturas(request,id=None):
    template_name='fac/facturas.html'

    detalle = {}
    clientes = Cliente.objects.filter(estado=True)

    if request.method == "GET":
        enc = FacturaEnc.objects.filter(pk=id).first()
        if not enc:
            encabezado = {
                'id':0,
                'fecha':datetime.today(),
                'cliente':0,
                'sub_total':0.00,
                'descuento':0.00,
                'total': 0.00
            }
            detalle=None
        else:
            encabezado = {
                'id':enc.id,
                'fecha':enc.fecha,
                'cliente':enc.cliente,
                'sub_total':enc.sub_total,
                'descuento':enc.descuento,
                'total':enc.total
            }

        detalle=FacturaDet.objects.filter(factura=enc)
        contexto = {"enc":encabezado,"det":detalle,"clientes":clientes}
        return render(request,template_name,contexto)

    #Para el Edit y guardar
    if request.method == "POST":
        cliente = request.POST.get("enc_cliente")
        fecha  = request.POST.get("fecha")
        cli=Cliente.objects.get(pk=cliente)

        # Para guardar
        if not id:
            enc = FacturaEnc(
                cliente = cli,
                fecha = fecha
            )
            if enc:
                enc.save()
                id = enc.id
        #Para editar
        else:
            enc = FacturaEnc.objects.filter(pk=id).first()
            if enc:
                enc.cliente = cli
                enc.save()
        # Mensaje de error
        if not id:
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Factura')
            return redirect("fac:factura_list")

        # Agregamos el detalle
        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("sub_total_detalle")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Producto.objects.get(codigo=codigo)
        det = FacturaDet(
            factura = enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total
        )

        if det:
            det.save()

        return redirect("fac:factura_edit",id=id)

    return render(request,template_name,contexto)


class ProductoView(inv.ProductoView):
    template_name="fac/buscar_producto.html"


def borrar_detalle_factura(request, id):
    template_name = "fac/factura_borrar_detalle.html"

    det = FacturaDet.objects.get(pk=id)

    if request.method=="GET":
        context={"det":det}

    # importar authenticate no olvidar
    if request.method == "POST":
        usr = request.POST.get("usuario")
        pas = request.POST.get("pass")

        # Instanciamos el usuario
        user = authenticate(username=usr, password=pas)

        if not user:
            return HttpResponse("Usuario o Clave Incorrecta")

        if not user.is_active:
            return HttpResponse("Usuario Inactivo")

        if user.is_superuser or user.has_perm("fac.sup_caja_facturadet"):
            # Si quitamos el id django crea un registro nuevo
            det.id = None
            det.cantidad = (-1 * det.cantidad)
            det.sub_total = (-1 * det.sub_total)
            det.descuento = (-1 * det.descuento)
            det.total = (-1 * det.total)
            det.save()

            return HttpResponse("ok")

        return HttpResponse("Usuario no autorizado")

    return render(request,template_name,context)