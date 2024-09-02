"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from carros.views import carros_view, new_car_view
from Mecanico.views import mecanico_view, new_mecanico_view
from accounts.views import register_view, login_view, logout_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('carros/', carros_view, name='cars_list'),
    path('mecanico/', mecanico_view, name='mecanico_list'),
    path('new_car/', new_car_view, name='new_car'),
    path('new_mecanico/', new_mecanico_view, name='new_mecanico'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
