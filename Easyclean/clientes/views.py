from django.shortcuts import render

# Create your views here.
def clienteHome(request):
    return render(request, 'clientehome.html')

def clienteOrden(request):
    return render(request, 'clienteorden.html')

def clienteServicio(request):
    return render(request, 'clienteservicio.html')

def clienteCarro(request):
    return render(request, 'clientecarro.html')