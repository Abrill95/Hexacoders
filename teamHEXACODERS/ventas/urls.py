from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import CustomLoginView, dashboard

app_name = 'ventas'
urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('clientes/', views.listar_clientes, name='clientes'),
    path('proveedores/', views.listar_proveedores, name='proveedores'),
    path('', views.listar_ventas, name='ventas'),
]
