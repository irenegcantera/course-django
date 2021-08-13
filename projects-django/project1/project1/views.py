from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
#from django.template.loader import get_template
from django.shortcuts import render

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
    
    #doc_externo=open("C:/Users/irene/Documents/GitHub Projects/projects-django/project1/project1/templates/miPlantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close() 
    #ctx=Context({'nombre': p1.nombre, 'apellido' : p1.apellido, 'fecha_actual' : fecha, 'temas' : lista_temas}) # contexto que puede recibir diccionarios
    #documento=plt.render(ctx) # renderizar

    #doc_externo=loader.get_template('miPlantilla.html')
    #documento=doc_externo.render({'nombre': p1.nombre, 'apellido' : p1.apellido, 'fecha_actual' : fecha, 'temas' : lista_temas}) 

    #return HttpResponse(documento)

    # request, nombre de la plantilla, contexto
    return render(request,'miPlantilla.html',{'nombre': p1.nombre, 'apellido' : p1.apellido, 'fecha_actual' : fecha, 'temas' : lista_temas})

def curso_django(request):

    fecha=datetime.datetime.now()
    return render(request, 'curso_django.html', {'dame_fecha' : fecha})



def despedida(request): # segunda vista
    return HttpResponse("Hasta luego, alumnos de Django!")

def dame_fecha(request): # tercera vista
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales: %s 
    </h2>
    </body>
    </html>""" % fecha_actual # marcador de posición
    return HttpResponse(documento)

def calcular_edad(request, edad_actual, year): # cuarta vista
    periodo=year-2021
    edad_futura= edad_actual+periodo
    documento="<html><body><h3>En el año %s tendrás %s años</h3></body></html>" %(year,edad_futura)
    return HttpResponse(documento)


