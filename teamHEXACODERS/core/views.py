from django.shortcuts import HttpResponse, render
from .models import Producto
from django.core.paginator import Paginator


def home(request):
    return render(request, "core/index.html")


def acercade(request):
    return render(request, "core/acercade.html")


def contacto(request):
    return render(request, "core/contacto.html")


def productos(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 12)  # Muestra 28 productos por página

# Obteniene el número de página de la solicitud
    page_number = request.GET.get('page')

    # Obtiene los productos para esa página
    productos_page = paginator.get_page(page_number)  #
    return render(request, "core/productos.html", {'productos': productos_page})

#base.html
def base(request):
    return render(request, "core/base.html")


