from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from AppCoder.forms import BuscarPelicula, PeliculasForm
from AppCoder.models import Peliculas


# Create your views here.


# Vistas "Inicio".
def inicio(request):
    return render(request, "index.html")


# Vistas "Peliculas"

def buscar_peliculas(request):
    buscar_pelicula = []
    if request.method == 'POST':
        name = request.POST.get('name')
        buscar_pelicula = Peliculas.objects.filter(name__icontains=name)
    context = {
        "my_form": BuscarPelicula(),
        'peliculas': buscar_pelicula,
    }

    return render(request, "AppCoder/peliculas/buscar.html", context)


def leer_peliculas(request):
    peliculas = Peliculas.objects.all()
    context = {
        'peliculas': peliculas
    }
    return render(request, 'AppCoder/peliculas/leer_peliculas.html', context)

@login_required
def crear_pelicula(request):
    if request.method == 'POST':
        my_form = PeliculasForm(request.POST, files=request.FILES)
        if my_form.is_valid():
            data = my_form.cleaned_data

            pelis_data = Peliculas(name=data.get('name'), synopsis=data.get('synopsis'), year=data.get('year'),
                                   gener=data.get('gener'), image=data.get('image'), trailer=data.get('trailer'),
                                   rating=data.get("rating"))
            pelis_data.save()

            return redirect('AppLeer')
        else:
            return redirect('AppInicio')

    context = {
        'peliculas_form': PeliculasForm()
    }

    return render(request, 'AppCoder/peliculas/crear.html', context)

@login_required
def grabar_pelicula(request):
    if request.method == 'POST':
        my_form = PeliculasForm(request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data

            pelicula_data = Peliculas(name=data.get('name'), synopsis=data.get('synopsis'), year=data.get('year'),
                                      gener=data.get('gener'), image=data.get('image'), trailer=data.get('trailer'),
                                      rating=data.get("rating"))
            pelicula_data.save()

    return redirect('AppLeer')

@login_required
def editar_pelicula(request, id):
    pelicula = Peliculas.objects.get(id=id)

    if request.method == 'POST':
        my_form = PeliculasForm(request.POST, files=request.FILES)
        if my_form.is_valid():
            data = my_form.cleaned_data

            pelicula.name = data.get('name')
            pelicula.synopsis = data.get('synopsis')
            pelicula.year = data.get('year')
            pelicula.gener = data.get('gener')
            pelicula.image = data.get('image')
            pelicula.trailer = data.get('trailer')
            pelicula.rating = data.get('rating')

            pelicula.save()

        return redirect('AppLeer')

    peliculas_form = PeliculasForm(initial={'name': pelicula.name, 'synopsis': pelicula.synopsis, 'year': pelicula.year, 'gener': pelicula.gener,
                     'image': pelicula.image, 'trailer': pelicula.trailer, 'rating': pelicula.rating})

    context = {

        'peliculas_form': peliculas_form
    }
    return render(request, 'AppCoder/peliculas/editar.html', context)


@login_required
def eliminar_pelicula(request, id):
    pelicula = Peliculas.objects.get(id=id)
    pelicula.delete()

    # peliculas = Peliculas.objects.all()

    # context = {
    #     'peliculas': peliculas
    # }

    return redirect('AppLeer')


# Vistas "Novedades"

def novedades(request):
    return render(request, "AppCoder/novedades/novedades.html")


# Vistas "About Us"

def contacto(request):
    return render(request, "AppCoder/sobreNosotros/contacto.html")


def nosotros(request):
    return render(request, "AppCoder/sobreNosotros/nosotros.html")


# Vistas "Plataformas"

def plataformas(request):
    return render(request, "AppCoder/plataformas/plataformas.html")
