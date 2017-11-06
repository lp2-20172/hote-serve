from django.db import models
from .area import Area
from core.models import Person


class Trabajador(models.Model):

    cargo = models.CharField(max_length=15)
    estado = models.BooleanField(initial=True)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaFind = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    area = models.ForeignKey(Area)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.cargo)
