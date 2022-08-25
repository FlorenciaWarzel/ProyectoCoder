from django import forms


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
