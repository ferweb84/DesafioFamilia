from django.urls import path, include
from.views import familia, profesion, ubicacion


urlpatterns = [
    path('AppFlia/',include('AppFlia.urls')),
    path('agrega-familia/<nombre>/<parentesco>/<dni>/',familia),
    path('agrega-profesion/<universidad>/<facultad>/<email>/',profesion),
    path('agrega-ubicacion/<pais>/<provincia>/<horario>/',ubicacion)
    
]
