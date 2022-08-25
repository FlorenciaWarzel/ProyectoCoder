from django.urls import path
from AppCoder.views import *

urlpatterns = [
     path('', inicio, name='AppInicio'),
     path('buscar', buscar_peliculas, name='AppBuscar'),
     path('novedades', novedades, name='AppNovedades'),
     path('nosotros', nosotros, name='AppNosotros'),
     path('plataformas', plataformas, name='AppPlataformas'),
     path('contacto', contacto, name='AppContacto'),


     #url cursos
     path('peliculas/', leer_peliculas, name='AppLeer'),
     path('pelicula/crear', crear_pelicula, name='AppCrear'),
     path('pelicula/editar/<nombre>', editar_pelicula, name='AppEditar')



]
