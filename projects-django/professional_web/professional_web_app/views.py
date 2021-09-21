from django.shortcuts import render, HttpResponse
from servicesapp.models import Service

# Create your views here.

def home(request):
    return render(request,"professional_web_app/home.html") # lo que muestra

def career(request):
    return render(request,"professional_web_app/career.html")

def service(request):
    services=Service.objects.all()
    return render(request, "professional_web_app/service.html", {"services": services})

def portfolio(request):
    return render(request,"professional_web_app/portfolio.html")

def news(request):
    return render(request,"professional_web_app/news.html")

def contact(request):
    return render(request,"professional_web_app/contact.html")