from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact(request):
    form_contact=ContactForm();
    # si se envia un contenido lo guardamos
    if(request.method == 'POST'):
        form_contact = ContactForm(data=request.POST)
        # si es valido el contenido
        if form_contact.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            return redirect("/contact/?valid")


    return render(request,"contacto/contact.html",{'form':form_contact})