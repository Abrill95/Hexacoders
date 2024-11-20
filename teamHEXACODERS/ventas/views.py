from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Cliente, Proveedor,Venta
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView

def productos(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 12)  # Muestra 28 productos por página

    # Obteniene el número de página de la solicitud
    page_number = request.GET.get('page')

    # Obtiene los productos para esa página
    productos_page = paginator.get_page(page_number)  #
    return render(request, "productos.html", {'productos': productos_page})

#Productos
class ProductoListView(ListView):
    model=Producto
    template_name='lista_productos.html'
    context_object_name='productos'
    def get_queryset(self):
        query = self.request.GET.get('q','')
        if query:
            return Producto.objects.filter(
                Q(codigo__icontains=query) |
                Q(nombre__icontains=query) |
                Q(precio__icontains=query)
            )
        return Producto.objects.all()

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['codigo', 'nombre', 'descripcion','precioAnterior','precio',
    'disponible', 'cantidad','imagen_principal','proveedores']
    template_name = 'forms/producto_form.html'
    success_url = reverse_lazy('ventas:lista_productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['codigo', 'nombre', 'descripcion','precioAnterior','precio',
              'disponible', 'cantidad','imagen_principal','proveedores']
    template_name = 'forms/producto_update_form.html'
    success_url = reverse_lazy('ventas:lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'forms/confirm_delete.html'
    success_url = reverse_lazy('ventas:lista_productos')


# ListView cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        query = self.request.GET.get('q','')
        if query:
            return Cliente.objects.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(email__icontains=query) |
                Q(celular__icontains=query)
            )
        return Cliente.objects.all()

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email','celular','foto']
    template_name = 'forms/cliente_form.html'
    success_url = reverse_lazy('ventas:clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    template_name = 'forms/cliente_update_form.html'
    success_url = reverse_lazy('ventas:clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'forms/confirm_delete.html'
    success_url = reverse_lazy('ventas:clientes')



class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'lista_proveedores.html'
    context_object_name = 'proveedores'

    def get_queryset(self):
        query = self.request.GET.get('q','')
        if query:
            return Proveedor.objects.filter(
                Q(nombre__icontains=query) | Q(email__icontains=query)
            )
        return Proveedor.objects.all()

class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ['nombre', 'email']
    template_name = 'forms/proveedor_form.html'
    success_url = reverse_lazy('ventas:proveedores')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ['nombre', 'email']
    template_name = 'forms/proveedor_form.html'
    success_url = reverse_lazy('ventas:proveedores')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'forms/confirm_delete.html'
    success_url = reverse_lazy('ventas:proveedores')



def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})
