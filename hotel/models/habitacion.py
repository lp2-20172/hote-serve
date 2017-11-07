from django.db import models
from .categoria import Categoria


class Habitacion(models.Model):

    amueblado = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10)
    estado = models.CharField(max_length=1)
    foto = models.ImageField(blank=True)
    categoriaHabitacion = models.ForeignKey(Categoria)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s' % (self.amueblado)
