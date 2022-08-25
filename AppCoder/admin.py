from django.contrib import admin

# Register your models here.
from AppCoder.models import Peliculas, Plataformas, News

admin.site.register(Peliculas)
admin.site.register(Plataformas)
admin.site.register(News)
