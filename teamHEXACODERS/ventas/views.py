from django.shortcuts import render
from .models import Producto, Cliente, Proveedor,Venta
from django.core.paginator import Paginator

def productos(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 12)  # Muestra 28 productos por página

    # Obteniene el número de página de la solicitud
    page_number = request.GET.get('page')

    # Obtiene los productos para esa página
    productos_page = paginator.get_page(page_number)  #
    return render(request, "productos.html", {'productos': productos_page})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {'productos': productos})


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})
