from django.shortcuts import render

# Create your views here.
def buscar_producto(request):
    return render(request, "search_product_form.html")
