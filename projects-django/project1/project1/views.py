from django.http import HttpResponse
import datetime

def saludo(request): # primera vista, devuelve una respuesta
    documento="<html><body><h1>Hola, alumnos! Esta es nuestra primera página con Django</h1></body></html>"
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


