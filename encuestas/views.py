from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.

def update(data):
    return HttpResponse("UPDATE - Hello World from Django for Codo a Codo 4.0")

def create(data):
    return HttpResponse("CREATE - Hello World from Django for Codo a Codo 4.0")

def delete(data):
    return HttpResponse("DELETE - Hello World from Django for Codo a Codo 4.0")

def read(data):
    print(data)
    return HttpResponse("READ - Hello World from Django for Codo a Codo 4.0")

def saludo(request):
    # myUsers = User.objects.all()
    # for user in myUsers:
    #     print(user.username)
    # return HttpResponse("Hello World from Django for Codo a Codo 4.0"

    myResponse = HttpResponse("Hello World from Django for Codo a Codo 4.0")

    if request.method == "GET":
        myResponse = read(request)
    elif request.method == "PUT":
        myResponse = update(request)
    elif request.method == "DELETE":
        myResponse = delete(request)
    else: # Que method es?POST
        myResponse = create(request)

    return myResponse


def diego(request):
    return HttpResponse("Soy Diego del team 5")

def home(request):
    return HttpResponse("Bienvenido al Home")