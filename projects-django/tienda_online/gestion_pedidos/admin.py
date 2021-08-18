from django.contrib import admin
from gestion_pedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','email','telefono') # información en la tabla
    search_fields=('nombre','telefono') # buscar registro por un campo

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('seccion',) # filtrar campo

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha')
    list_filter=('fecha',) # filtrado por el tiempo que tiene el pedido
    date_hierarchy='fecha' # filtrado por mes y año

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
