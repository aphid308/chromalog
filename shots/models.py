from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField("Manufacturer Name", max_length=50)
    country = models.CharField("Country", max_length=50)
    notes = models.TextField()

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.name

class Film(models.Model):
    mfg = models.ForeignKey(Manufacturer, on_delete="CASCADE")
    stock = models.CharField("Film Stock", max_length=50)
    iso = models.CharField("iso", max_length=50)
    film_format = models.CharField("Film Format", max_length=50)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"

    def __str__(self):
        return str(self.mfg) + ": " + str(self.stock)


