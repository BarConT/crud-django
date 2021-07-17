from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("Hello World from Django for Codo a Codo 4.0")

def diego(request):
    return HttpResponse("Soy Diego del team 5")
