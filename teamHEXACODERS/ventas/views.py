from django.shortcuts import render

from django.shortcuts import render
from .models import Producto
from django.core.paginator import Paginator

def productos(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 12)  # Muestra 28 productos por página

    # Obteniene el número de página de la solicitud
    page_number = request.GET.get('page')

    # Obtiene los productos para esa página
    productos_page = paginator.get_page(page_number)  #
    return render(request, "productos.html", {'productos': productos_page})
