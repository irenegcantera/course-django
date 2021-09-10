from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20)
    surname1=models.CharField(max_length=30)
    surname2=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    tel_no=models.IntegerField()
    message=models.TextField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='person'
        verbose_name_plural='people'
        ordering=['created']
    
    def __str__(self):
        return 'Nombre: ' + self.name + '\nApellido: '+ self.surname1 + '\nMensaje: ' + self.message


