from django.urls import path, include

from .views import (
    #Clientes
    ClienteView,
    ClienteNew,
    ClienteEdit,
    clienteInactivar,
    FacturaView,
    facturas,
    ProductoView,
    borrar_detalle_factura,
)

from .reportes import imprimir_factura_recibo

app_name = "fac_app"

urlpatterns = [
    #Clientes
    path('Clientes/', ClienteView.as_view(), name="cliente_list"),
    path('Clientes/new/', ClienteNew.as_view(), name='cliente_new'),
    path('Clientes/edit/<int:pk>/', ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/estado/<int:id>', clienteInactivar, name="cliente_inactivar"),
    #Facturas
    path('Facturas/', FacturaView.as_view(), name="factura_list"),
    path('Facturas/new/', facturas, name="factura_new"),
    path('facturas/edit/<int:id>',facturas, name="factura_edit"),

    path('facturas/buscar-producto', ProductoView.as_view(), name="factura_producto"),

    path('facturas/borrar-detalle/<int:id>', borrar_detalle_factura, name="factura_borrar_detalle"),

    path('facturas/imprimir/<int:id>', imprimir_factura_recibo, name="factura_imprimir_one"),
]
