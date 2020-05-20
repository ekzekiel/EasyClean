from django.shortcuts import render

# Create your views here.
def colaboradorHome(request):
    return render(request, 'colaboradorhome.html')