from django.contrib import admin
from .models import Cliente, Proveedor, Producto, ImagenProducto, Venta



class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1  # Número de imágenes adicionales que se pueden agregar en línea


class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]
    list_display = ('nombre', 'precio', 'disponible','precioAnterior')
    list_filter = ('disponible',)
    search_fields = ('nombre', 'descripcion')

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)