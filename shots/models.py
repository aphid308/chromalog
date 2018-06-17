from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField("Manufacturer Name", max_length=50)
    country = models.CharField("Country", max_length=50, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.name

class Film(models.Model):
    mfg = models.ForeignKey(Manufacturer, on_delete="CASCADE")
    stock = models.CharField("Film Stock", max_length=50)
    iso = models.IntegerField()
    film_format = models.CharField("Film Format", max_length=50)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"

    def __str__(self):
        return str(self.mfg) + ": " + str(self.stock)

class Shot(models.Model):
    title = models.CharField("Title", max_length=50)
    film = models.ForeignKey(Film, on_delete="PRESERVE")
    image = models.ImageField(upload_to='shot_upload/', max_length=100)
    class Meta:
        verbose_name = "Shot"
        verbose_name_plural = "Shots"

    def __str__(self):
        return str(self.title)

