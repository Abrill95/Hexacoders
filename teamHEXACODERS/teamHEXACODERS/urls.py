from core import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('admin/', admin.site.urls),
                  path('acercade/', views.acercade, name='acercade'),
                  path('contacto/', views.contacto, name='contacto'),
                  path('ventas/', include('ventas.urls')),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
