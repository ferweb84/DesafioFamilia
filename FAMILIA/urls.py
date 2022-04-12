"""FAMILIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AppFlia.views import profesion
from AppFlia.views import ubicacion
from.views import saludo, segundosaludo,saluda_con_nombre,templateFamilia
from AppFlia.views import familia, profesion, ubicacion

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('saludo/', saludo),
    # path('segundosaludo/', segundosaludo),
    # path('saluda_con_nombre/<nombre>/<edad>/', saluda_con_nombre),
    path('templateFamilia/<nombre>/',templateFamilia),
    path('agrega-familia/<nombre>/<parentesco>/<dni>/',familia),
    path('agrega-profesion/<universidad>/<facultad>/<email>/',profesion),
    path('agrega-ubicacion/<pais>/<provincia>/<horario>/',ubicacion)
    
]
