from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, "core/index.html")


def acercade(request):
    return render(request, "core/acercade.html")
