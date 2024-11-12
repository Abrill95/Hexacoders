from django.contrib import admin
from .models import Producto, ImagenProducto



class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1  # Número de imágenes adicionales que se pueden agregar en línea


class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]
    list_display = ('nombre', 'precio', 'disponible','precioAnterior')
    list_filter = ('disponible',)
    search_fields = ('nombre', 'descripcion')


admin.site.register(Producto, ProductoAdmin)
