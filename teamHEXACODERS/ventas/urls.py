from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'ventas'
urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.listar_clientes, name='lista_clientes'),
    path('proveedores/', views.listar_proveedores, name='lista_proveedores'),
    path('ventas/', views.listar_ventas, name='lista_ventas'),
]
