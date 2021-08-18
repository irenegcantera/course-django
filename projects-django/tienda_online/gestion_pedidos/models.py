from django.db import models

# Create your models here.
# Clase por cada tabla de la base de datos, no es necesario trabajar con sql

class Clientes(models.Model):
    # campo y tipo de campo, propiedades
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    # hay que volver a hacer migraciones siempre que modifiquemos los modelos
    def __str__(self):
        return 'El nombre es %s la sección de %s y el precios es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
