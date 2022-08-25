from django.db import models

# Create your models here.
class Peliculas(models.Model):
    name = models.CharField(max_length=40)
    synopsis = models.CharField(max_length=600)
    year = models.IntegerField()
    gener = models.CharField(max_length=40)
    image = models.ImageField(blank=True, null=True)
    trailer = models.URLField()
    rating = models.FloatField()

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
