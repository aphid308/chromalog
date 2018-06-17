from django.contrib import admin
from .models import Manufacturer, Film

# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    list_display = ('stock', 'mfg', 'iso', 'film_format')

admin.site.register(Manufacturer)
admin.site.register(Film, FilmAdmin)
