from clientes import views
from django.conf.urls import url
from django.urls import path, include



urlpatterns = [

   
    #path('', views.clienteHome, name="index"),
    path('clienteHome/', views.clienteHome, name="clienteHome"),
    path('clienteOrden/',  views.clienteOrden, name="clienteOrden"),
    path('clienteServicio/', views.clienteServicio, name="clienteServicio"),
    path('clienteCarro/', views.clienteCarro, name="clienteCarro"),
    
 

]
