from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): # primera vista, devuelve una respuesta

    p1=Persona("Prueba","Con Clases")
    
    #nombre="Irene"
    #apellido="González"
    fecha=datetime.datetime.now()

    lista_temas=['Plantillas','Modelos','Formularios','Vistas','Despliegue']
    
    doc_externo=open("C:/Users/irene/Documents/GitHub Projects/projects-django/project1/project1/template/miPlantilla.html")

    plt=Template(doc_externo.read())
    doc_externo.close() 
    ctx=Context({'nombre': p1.nombre, 'apellido' : p1.apellido, 'fecha_actual' : fecha, 'temas' : lista_temas}) # contexto que puede recibir diccionarios
    documento=plt.render(ctx) # rederizar

    return HttpResponse(documento)

def despedida(request): # segunda vista
    return HttpResponse("Hasta luego, alumnos de Django!")

def dameFecha(request): # tercera vista
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales: %s 
    </h2>
    </body>
    </html>""" % fecha_actual # marcador de posición
    return HttpResponse(documento)

def calcularEdad(request, edadActual, year): # cuarta vista
    periodo=year-2021
    edadFutura= edadActual+periodo
    documento="<html><body><h3>En el año %s tendrás %s años</h3></body></html>" %(year,edadFutura)
    return HttpResponse(documento)


