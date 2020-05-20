from administrador import views
from django.conf.urls import url
from django.urls import path, include



urlpatterns = [

   
    #path('', views.clienteHome, name="index"),
    path('adminHome/', views.adminHome, name="adminHome"),
    path('adminServicio/',  views.adminServicio, name="adminServicio"),
    path('adminColaborador/', views.adminColaborador, name="adminColaborador"),
    path('adminAsignar/', views.adminAsignar, name="adminAsignar"),
    path('addServicioForm/', views.addServicioForm, name="addServicioForm"),
    path('crearServicio/', views.crearServicio, name="crearServicio"),
    path('guardarServicio/', views.guardarServicio, name="guardarServicio")
]
