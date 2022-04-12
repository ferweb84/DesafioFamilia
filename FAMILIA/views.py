from contextvars import Context
from fileinput import close

from django import template
from django.template import Template
from django.http import HttpResponse
from django.template import Context
from datetime import datetime
from django.template import loader

def saludo (recuest):
    return HttpResponse ('Hola familia')

def segundosaludo (request):
    return HttpResponse ('saludo desde mi segundo template')

def saluda_con_nombre (request, nombre,edad):
    return HttpResponse (f'Hola {nombre}! ya tenes {edad} años')

def templateFamilia (recuest,nombre,parentesco,dni):

    dni=[31056772,27125684,26854122]

    # miHtml = open (r'C:\Users\Luciano\Desktop\Python Desafio MVT\FAMILIA\FAMILIA\templates\templateFlia.html')

    # plantilla= Template (miHtml.read())

    # miHtml.close()

    # miContexto =Context({'name':nombre,"ahora":datetime.now(), "notas":listaNotas})

    plantilla=loader.get_template ('templateFlia.html')
    # return HttpResponse (plantilla.render({'name':nombre,'ahora':datetime.now(), 'notas':listaNotas}))
    return HttpResponse (plantilla.render({'name':nombre,'parentesco':parentesco, 'dni':dni}))
