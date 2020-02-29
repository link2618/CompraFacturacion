from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

# para redireccionar a un sitio
from django.urls import reverse_lazy
# Mensajes para vistas creadas en def
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Mensajes para vistas creadas en class
from django.contrib.messages.views import SuccessMessageMixin
#decoradores para el LoginRequire y PermissionRequired para trabajarlos en funciones
from django.contrib.auth.decorators import  login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import  CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

from bases.views import SinPrivilegios

# Create your views here.
class CategoriaView(LoginRequiredMixin, SinPrivilegios, ListView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


# El CreateView da por hecho que se va hacer un insert en la BD
class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = CategoriaForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"
    success_message = "Categoria creada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


# Para editar es lo mismo que para crear pero se cambia el CreateView por UpdateView
class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = CategoriaForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"
    success_message = "Categoria actualizada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Para borrar categoria de la BD, No se recomienda usar esta forma de borrar por que se pierde el historico
class CategoriaDel(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, DeleteView):
    permission_required = "inv.delete_categoria"
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"
    success_message = "Categoria eliminada satisfactoriamente."


#----------------------------------------------- VISTAS DE SUB CATEGORIA --------------------------------------
class SubCategoriaView(LoginRequiredMixin, SinPrivilegios, ListView):
    # Permiso para ver la vista, mayor seguridad para no saltar el permiso por url
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


# El CreateView da por hecho que se va hacer un insert en la BD
class SubCategoriaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    permission_required = "inv.add_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = SubCategoriaForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"
    success_message = "Sub Categoria agregada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


# Para editar es lo mismo que para crear pero se cambia el CreateView por UpdateView
class SubCategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    permission_required = "inv.change_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = SubCategoriaForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"
    success_message = "Sub Categoria actulizada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Para borrar categoria de la BD, No se recomienda usar esta forma de borrar por que se pierde el historico
class SubCategoriaDel(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, DeleteView):
    permission_required = "inv.delete_subcategoria"
    model = SubCategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"
    success_message = "Sub Categoria eliminada satisfactoriamente."


#------------------------------------------- VISTAS DE MARCA ------------------------------------------
class MarcaView(LoginRequiredMixin, SinPrivilegios, ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


# El CreateView da por hecho que se va hacer un insert en la BD
class MarcaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    permission_required = "inv.add_marca"
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = MarcaForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"
    success_message = "Marca agregada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


# Para editar es lo mismo que para crear pero se cambia el CreateView por UpdateView
class MarcaEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    permission_required = "inv.change_marca"
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = MarcaForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"
    success_message = "Marca actualizada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Para borrar categoria de la BD, No se recomienda usar esta forma de borrar por que se pierde el historico
@login_required(login_url='/login/') #seguridad para no ingresar por url
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')#seguridad para no ingresar por url sin permiso
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    # Mostramos el contenido que vamos a eliminar
    if request.method=='GET':
        contexto = {'obj':marca}

    # Cambiamos el estado de True a False
    if request.method=='POST':
        marca.estado = False
        marca.save()
        # imprimimos un mensaje por jqury Confirm
        messages.success(request, 'Marca Inactivada.')
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)


#------------------------------------------- VISTAS DE UNIDAD DE MEDIDA ------------------------------------------
class UMView(LoginRequiredMixin, SinPrivilegios, ListView):
    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class UMNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    permission_required = "inv.add_unidadmedida"
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = UMForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:um_list")
    login_url = "bases:login"
    success_message = "Unidad de Medida agregada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    permission_required = "inv.change_unidadmedida"
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = UMForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:um_list")
    login_url = "bases:login"
    success_message = "Unidad de Medida actualizada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Para borrar categoria de la BD, No se recomienda usar esta forma de borrar por que se pierde el historico
@login_required(login_url='/login/') #seguridad para no ingresar por url
@permission_required('inv.change_unidadmedida', login_url='bases:sin_privilegios')#seguridad para no ingresar por url sin permiso
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")

    # Mostramos el contenido que vamos a eliminar
    if request.method=='GET':
        contexto = {'obj':um}

    # Cambiamos el estado de True a False
    if request.method=='POST':
        um.estado = False
        um.save()
        # imprimimos un mensaje por jqury Confirm
        messages.success(request, 'Unidad de Medida Inactivada.')
        return redirect("inv:um_list")

    return render(request, template_name, contexto)


#------------------------------------------- VISTAS DE PRODUCTOS ------------------------------------------
class ProductoView(LoginRequiredMixin, SinPrivilegios, ListView):
    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class ProductoNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, CreateView):
    permission_required = "inv.add_producto"
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = ProductoForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"
    success_message = "Producto agregado satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, UpdateView):
    permission_required = "inv.change_producto"
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    # formulario que se va a renderizar
    form_class = ProductoForm
    # Es cuando se le da click al boton submit para redireccionar y tener mayor seguridad
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"
    success_message = "Producto actualizada satisfactoriamente."

    # vamos a tomar el usuario logeado para actualizar los campos automaticos
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


# Para borrar categoria de la BD, No se recomienda usar esta forma de borrar por que se pierde el historico
@login_required(login_url='/login/') #seguridad para no ingresar por url
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')#seguridad para no ingresar por url sin permiso
def producto_inactivar(request, id):
    pro = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not pro:
        return redirect("inv:producto_list")

    # Mostramos el contenido que vamos a eliminar
    if request.method=='GET':
        contexto = {'obj':pro}

    # Cambiamos el estado de True a False
    if request.method=='POST':
        pro.estado = False
        pro.save()
        # imprimimos un mensaje por jqury Confirm
        messages.success(request, 'Producto Inactivado.')
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)
