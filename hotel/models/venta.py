from django.db import models
from core.models import User
from .cliente import Cliente


class Venta(models.Model):

    nro_doc = models.CharField(max_length=15)
    numeroReservacion = models.IntegerField()
    vendedor = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.nro_doc)
