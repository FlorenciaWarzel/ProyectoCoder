from django import forms
from django.db import models


class BuscarPelicula(forms.Form):
    name = forms.CharField(max_length=40)


class PeliculasForm(forms.Form):
    name = forms.CharField(max_length=40)
    synopsis = forms.CharField(max_length=600)
    year = forms.IntegerField()
    gener = forms.CharField(max_length=40)
    image = forms.ImageField()
    trailer = forms.URLField()
    rating = forms.FloatField()

class Registro(models.Model):
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=600)
    email = models.EmailField()
