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

# Modificando para usar ListView proveedor
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



# Usando CreateView pra cliente
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('ventas:clientes')

# Usando  UpdateView para cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('ventas:clientes')

# Usando DeleteView para cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('ventas:clientes')

# Usando Create Vieew para Proveedor
class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ['nombre', 'email']
    template_name = 'proveedor_form.html'
    success_url = reverse_lazy('ventas:proveedores')

# Usando  UpdateView para Proveedor
class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ['nombre', 'email']
    template_name = 'proveedor_form.html'
    success_url = reverse_lazy('ventas:proveedores')

# Usando DeleteView para Proveedor
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor_confirm_delete.html'
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
