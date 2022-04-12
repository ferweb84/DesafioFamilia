import email
from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre=models.CharField('nombre',max_length=40)
    parentesco=models.CharField('integrante',max_length=50)
    dni=models.IntegerField('dni')
    

class Profesion(models.Model):
    universidad=models.CharField('universidad',max_length=100)
    facultad=models.CharField('facultad',max_length=100)
    email=models.EmailField('email')

class Ubicacion(models.Model):
    pais=models.CharField('pais',max_length=50)
    Provincia=models.CharField('provincia',max_length=50)
    horario=models.DateField('horario')