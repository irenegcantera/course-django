from django.http.response import HttpResponse
from django.shortcuts import render
from gestion_pedidos.models import Articulos

# Create your views here.
def buscar_producto(request):
    return render(request, "search_product_form.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r" % request.GET["prd"]
        producto=request.GET["prd"]
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        return render(request, "resultado_busqueda.html", {"articulos": articulos, "query": producto}) # html que muestra el resultado
    else:
        mensaje="No has introducido un artículo"
    return HttpResponse(mensaje)
