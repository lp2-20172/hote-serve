from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=60)
    fotos = models.ImageField(blank=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % (self.nombre)
