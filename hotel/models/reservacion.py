from django.db import models
from .pago import Forma_de_pago


class Reservacion(models.Model):

    nro_doc_referencia = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    forma_de_pago = models.ForeignKey(Forma_de_pago)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.nro_doc)
