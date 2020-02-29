from django.contrib import admin

from .models import Proveedor

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'descripcion',
        'direccion',
        'contacto',
        'telefono',
        'email',
        'estado',
        'fc',
        'fm',
        'uc',
        'um',
    )
    # Atributo para buscar un campo
    search_fields = ('descripcion',)
    # Hacemos filtros
    list_filter = ('estado',)

admin.site.register(Proveedor, ProveedorAdmin)
