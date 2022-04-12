import email
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familia, Profesion, Ubicacion

# Create your views here.
def familia(request, nombre, parentesco, dni):

    mi_flia= Familia(nombre=nombre, parentesco=parentesco,dni=dni)
    mi_flia.save()

    return HttpResponse (f'Se genero familiar {mi_flia.nombre} con el parentesco {mi_flia.parentesco} y el dni {mi_flia.dni}')

def profesion(request, universidad, facultad, email):

    profesion= Profesion (universidad=universidad, facultad=facultad,email=email)
    profesion.save()

    return HttpResponse (f'Se genero universidad {universidad}, {facultad}, email {email}')

def ubicacion(request, pais, provincia, horario):

    ubicacion= Ubicacion(pais=pais, provincia=provincia,horario=horario)
    ubicacion.save()

    return HttpResponse (f'Se genero Ubicacion del familiar {ubicacion.pais} en la provincia o ciudad {ubicacion.Provincia} y el horario {ubicacion.horario}')
