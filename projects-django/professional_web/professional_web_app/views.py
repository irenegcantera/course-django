from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home") # lo que muestra

def career(request):
    return HttpResponse("Carrer")

def portfolio(request):
    return HttpResponse("Portfolio")

def news(request):
    return HttpResponse("News")

def contact(request):
    return HttpResponse("Contact")