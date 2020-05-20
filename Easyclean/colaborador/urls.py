from colaborador import views
from django.conf.urls import url
from django.urls import path



urlpatterns = [

   
    #path('', views.clienteHome, name="index"),
    path('colaboradorHome/', views.colaboradorHome, name="colaboradorHome"),
 

]