from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=60)
    imagen1 = models.ImageField(blank=True)
    imagen2 = models.ImageField(blank=True)
    imagen3 = models.ImageField(blank=True)
    precio = models.FloatField(default=0.0)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % (self.nombre)
