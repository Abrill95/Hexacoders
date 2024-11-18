from django.shortcuts import HttpResponse, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Vista para el Dashboard
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

# Vista para Login
class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True


def home(request):
    return render(request, "core/index.html")


def acercade(request):
    return render(request, "core/acercade.html")


def contacto(request):
    return render(request, "core/contacto.html")


#base.html
def base(request):
    return render(request, "core/base.html")
