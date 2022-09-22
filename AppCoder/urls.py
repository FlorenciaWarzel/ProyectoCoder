from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('', inicio, name='AppInicio'),
    path('buscar', buscar_peliculas, name='AppBuscar'),
    path('novedades', novedades, name='AppNovedades'),
    path('nosotros', nosotros, name='AppNosotros'),
    path('plataformas', plataformas, name='AppPlataformas'),
    path('contacto', contacto, name='AppContacto'),

    # url cursos
    path('peliculas/', leer_peliculas, name='AppLeer'),
    path('peliculas/crear', crear_pelicula, name='AppCrear'),
    path('peliculas/grabar', grabar_pelicula, name='AppGrabar'),
    path('peliculas/editar/<int:id>', editar_pelicula, name='AppEditar'),
    path('peliculas/eliminar/<int:id>', eliminar_pelicula, name='AppEliminar'),

]
