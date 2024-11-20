from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView, ClienteListView, ProveedorListView,ProductoCreateView,ProductoListView,ProductoDeleteView,ProductoUpdateView
app_name = 'ventas'
urlpatterns = [
    path('productos-venta/', views.productos, name='productos'),

    path('productos/', ProductoListView.as_view(), name='lista_productos'),

    path('productos/agregar/', ProductoCreateView.as_view(), name='producto_add'),

    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_edit'),

    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),


    # Modificando para usar ListView cliente
    path('clientes/', ClienteListView.as_view(), name='clientes'),
    #  Usando CreateViews para cliente
    path('clientes/agregar/', ClienteCreateView.as_view(), name='cliente_add'),
    # Usando UpdateView para cliente
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_edit'),
    # Usando DeleteView para cliente
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # ListView proveedor
    path('proveedores/', ProveedorListView.as_view(), name='proveedores'),
    #  Usando CreateViews para proveedor
    path('proveedores/agregar/', ProveedorCreateView.as_view(), name='proveedor_add'),
    # Usando UpdateView para proveedor
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_edit'),
    # Usando DeleteView para proveedor
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_delete'),



    path('proveedores/', views.listar_proveedores, name='proveedores'),
    path('lista_ventas/', views.listar_ventas, name='ventas'),
]
