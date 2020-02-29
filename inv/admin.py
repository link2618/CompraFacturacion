from django.contrib import admin

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'descripcion',
        'estado',
        'fc',
        'fm',
        'uc',
        'um',
    )
    # Atributo para buscar un campo
    search_fields = ('descripcion',)
    # Hacemos filtros
    list_filter = ('estado', 'fc',)
    # filto en la parte superior
    date_hierarchy="fc"

admin.site.register(Categoria, CategoriaAdmin)
