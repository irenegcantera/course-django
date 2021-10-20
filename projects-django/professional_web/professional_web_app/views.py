from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request,"professional_web_app/home.html") # lo que muestra

def career(request):
    return render(request,"professional_web_app/career.html")

def portfolio(request):
    return render(request,"professional_web_app/portfolio.html")