from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    form_contact=ContactForm();
    # si se envia un contenido lo guardamos
    if(request.method == 'POST'):
        form_contact = ContactForm(data=request.POST)
        # si es valido el contenido
        if form_contact.is_valid():
            nombre = request.POST.get('name')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')

            email = EmailMessage("Mensaje desde el proyecto",
                                "El usuario {} ha escrito un mensaje:\n\n{}".format(nombre, mensaje),
                                email,["your_email"],reply_to = [email])
            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?no-valid")

    return render(request,"contacto/contact.html",{'form':form_contact})