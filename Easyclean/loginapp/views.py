from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'index.html')


def servicios(request):
    return render(request,"servicios.html")

def registrarse(request):
    return render(request, "register.html")

def login(request):

    return render(request, "login.html")


