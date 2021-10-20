from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    form_contact=ContactForm();
    return render(request,"contacto/contact.html",{'form':form_contact})