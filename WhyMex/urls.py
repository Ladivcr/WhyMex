"""WhyMex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from WhyMex import views as local_views
from posts import views as post_views

#urlpatterns = [path('admin/', admin.site.urls),]

urlpatterns = [
    path('inicio/', post_views.main_menu, name="inicio"),
    path('registro/', post_views.register_problem, name='registrar_problema'),
    path('mapa/', post_views.show_map, name='mostrar_mapa'),
    path('contacto/', post_views.contact, name='contacto'),
    path('dudas/', post_views.help, name='ayuda'),
] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
