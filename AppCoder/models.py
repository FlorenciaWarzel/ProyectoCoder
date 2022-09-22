from django.db import models


# Create your models here.
class Peliculas(models.Model):
    name = models.CharField(unique=True, verbose_name='Título', max_length=40)
    synopsis = models.CharField(max_length=600, verbose_name='Reseña')
    year = models.IntegerField(verbose_name='Año')
    gener = models.CharField(max_length=40, verbose_name='Género')
    image = models.ImageField(verbose_name='Portada', null=True)
    trailer = models.URLField(verbose_name='Trailer')
    rating = models.FloatField(verbose_name='Calificación')

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    premier = models.CharField(max_length=40)
    image = models.ImageField(blank=True, null=True)


class Plataformas(models.Model):
    name = models.CharField(max_length=40)
    link = models.URLField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
