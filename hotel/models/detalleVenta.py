from django.db import models
from .venta import Venta
from .docType import Doc_Type


class DetalleVenta(models.Model):

    detalle = models.TextField(null=True, blank=True)
    venta = models.ForeignKey(Venta)
    doc_type = models.ForeignKey(Doc_Type)

    class Meta:
        verbose_name = "DetalleVenta"
        verbose_name_plural = "DetalleVentas"

    def __str__(self):
        return '%s' % (self.detalle)
