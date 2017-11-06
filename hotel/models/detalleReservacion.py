from django.db import models
from .habitacion import Habitacion


class DetalleReservacion (models.Model):

    asunto = models.CharField(max_length=10)
    fecha = models.DateTimeField(auto_now_add=True)
    habitacion = models.ForeignKey(Habitacion)

    class Meta:
        verbose_name = "DetalleReservacion"
        verbose_name_plural = "DetalleReservaciones"

    def __str__(self):
        return '%s' % (self.asunto)
