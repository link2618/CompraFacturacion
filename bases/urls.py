from django.urls import path, include
#Libreria para crear la ruta de login
from django.contrib.auth import views as auth_views

from bases.views import (
    Home,
    HomeSinPrivilegios,
    )

app_name = "bases_app"

#La url para que funcione debe llamarse desde el archivo principal de url
urlpatterns = [
    path('',Home.as_view(), name='home'),
    #Creacion de la ruta login y logout sin necesidad de crear vista
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
    #Vista de sin_privilegios
    path('sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios'),
]
