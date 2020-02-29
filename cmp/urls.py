from django.urls import path, include

from .views import (
    #Proveedores
    ProveedorView,
    ProveedorNew,
    ProveedorEdit,
    proveedor_inactivar,
    #ComprasEnc
    ComprasView,
    compras,
    CompraDetDelete,
)

app_name = "cmp_app"

urlpatterns = [
    #Proveedores
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new/', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>/', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>/', proveedor_inactivar, name='proveedor_inactivar'),
    #ComprasEnc
    path('compras/', ComprasView.as_view(), name='compras_list'),
    path('compras/new/', compras, name='compras_new'),
    path('compras/edit/<int:compra_id>', compras, name='compras_edit'),
    path('compras/<int:compra_id>/delete/<int:pk>/', CompraDetDelete.as_view(), name='compras_del'),
]
