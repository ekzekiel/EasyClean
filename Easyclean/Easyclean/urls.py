"""Easyclean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.views import auth_login, logout_then_login
from django.urls import path, include
from loginapp import views
#from clientes import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('servicios/', views.servicios, name="servicios"),
    path('login/', views.login, name="login"),
    path('registrarse/', views.registrarse, name="registro_cliente"),
    path('clientes/', include('clientes.urls')),
    path('colaborador/', include('colaborador.urls')),
    path('administrador/', include('administrador.urls')),
    #path('', views.clientes, name="index"),
    #path('clienteHome/', views.clienteHome, name="clienteHome"),
 

]