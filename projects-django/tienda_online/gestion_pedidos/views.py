from django.http.response import HttpResponse
from django.shortcuts import render
from gestion_pedidos.models import Articulos
from django.conf import settings
from django.core.mail import send_mail
from gestion_pedidos.forms import FormularioContacto

# Create your views here.
def buscar_producto(request):
    return render(request, "search_product_form.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r" % request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto) > 20:
            mensaje="El texto de búsqueda supera el límite."
        else: 
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultado_busqueda.html", {"articulos": articulos, "query": producto}) # html que muestra el resultado
    else:
        mensaje="No has introducido un artículo"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        mi_form=FormularioContacto(request.POST)
        if mi_form.is_valid():
            inform=mi_form.cleaned_data
            send_mail(inform['asunto'],inform['mensaje'],inform.get('email',''),['prueba@gmail.com'],)
            return render(request, 'gracias.html')
    else:
        mi_form=FormularioContacto()
    return render(request,'form_contacto.html',{'form':mi_form})

    # if request.method=="POST":
    #     subject=request.POST['asunto']
    #     message=request.POST['mensaje'] + " " + request.POST['email']
    #     email_from=settings.EMAIL_HOST_USER
    #     recipient_list=['cursos@pildorasinformaticas.es']
    #     send_mail(subject,message,email_from,recipient_list)
    #     return render(request, "gracias.html")
    # return render(request, "contacto.html")