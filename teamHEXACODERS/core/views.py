from django.shortcuts import HttpResponse, render
from django.core.paginator import Paginator


def home(request):
    return render(request, "core/index.html")


def acercade(request):
    return render(request, "core/acercade.html")


def contacto(request):
    return render(request, "core/contacto.html")


#base.html
def base(request):
    return render(request, "core/base.html")
