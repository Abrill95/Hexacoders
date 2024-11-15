from django.contrib import admin
from .models import Cliente, Proveedor, Producto, ImagenProducto, Venta

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'celular')
    search_fields = ('nombre', 'apellido', 'email', 'celular')
    filter_horizontal = ('favoritos',)

class VentaInline(admin.TabularInline):
    model = Venta
    extra = 1
    fields = ['producto', 'cliente', 'precio']
    autocomplete_fields = ['producto', 'cliente']

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'producto', 'cliente', 'precio')
    search_fields = ('producto__nombre', 'cliente__nombre')
    autocomplete_fields = ['producto', 'cliente']

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]
    list_display = ('nombre', 'precio', 'disponible','precioAnterior')
    list_filter = ('disponible',)
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('proveedores',)

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)
