from core import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import CustomLoginView, dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('acercade/', views.acercade, name='acercade'),
    path('contacto/', views.contacto, name='contacto'),
    path('ventas/', include('ventas.urls')),
                  path('login/', CustomLoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
                  path('dashboard/', dashboard, name='dashboard')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
