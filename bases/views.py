from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    TemplateView,
    )

# Create your views here.
#Los mixin siempre deben ir a la izquierda para tener mayor prioridad y realizar validaciones
class Home(LoginRequiredMixin, TemplateView):
    #busca en la carpeta templates
    template_name = 'bases/home.html'

    #Si no esta logeado se redirecciona
    login_url = 'bases:login'


class HomeSinPrivilegios(LoginRequiredMixin, TemplateView):
    template_name = 'bases/sin_privilegios.html'
    login_url = 'bases:login'


class SinPrivilegios(PermissionRequiredMixin):
    # que no se levante el error 403
    raise_exception = False
    redirect_field_name="redirect_to"

    #metodo que manipula o da permisos a las vistas
    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))
