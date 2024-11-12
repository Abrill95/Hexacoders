from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'ventas'
urlpatterns = [
    path('productos/', views.productos, name='productos'),
]
