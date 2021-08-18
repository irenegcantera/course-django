from django.contrib import admin
from gestion_pedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','email','telefono')

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
