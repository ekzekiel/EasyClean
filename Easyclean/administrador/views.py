from django.shortcuts import render, HttpResponse
from administrador.models import Servicio

# Create your views here.
def adminHome(request):
    return render(request, 'adminhome.html')

def adminColaborador(request):
    return render(request, 'admincolaborador.html')

def adminServicio(request):
    return render(request, 'adminservicio.html')

def adminAsignar(request):
    return render(request, 'adminasignarorden.html')

def addServicioForm(request):
    return render(request, 'addservicioform.html')

"""
def crearServicio(request):
    servicio = Servicio(
        nombre_servicio = 'barrer',
        descricion = 'casa',
        precio = 20000
    )

    servicio.save()

    return HttpResponse(f"Servicio creado:<strong>{servicio.nombre_servicio}")
"""


def guardarServicio(request):

    if request.method == 'POST':

        nombre_servicio = request.POST['nombre_servicio']
        descricion = request.POST['descricion']
        precio = request.POST['precio']

        servicio = Servicio(
            nombre_servicio = nombre_servicio,
            descricion = descricion,
            precio = precio
        )
        servicio.save()
        
        return HttpResponse(f"producto creado: <strong>{servicio.nombre_servicio}</strong>")
    else:
        return HttpResponse("<h2>no se ha podido crear el articulo</h2>")

def crearServicio(request):
    return render(request, 'addservicioform.html')
