from re import template
from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



# def login(request):
#     return render(request, 'login.html')

# def eventos(request):
#     return render(request, 'eventos.html')

