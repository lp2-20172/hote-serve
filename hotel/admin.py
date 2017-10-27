from django.contrib import admin
from hotel.models_raiz import Reservacion
from hotel.models.categoria import Categoria
from hotel.models_raiz import Habitacion
from hotel.models_raiz import DetalleReservacion
from hotel.models_raiz import Forma_de_pago
from hotel.models_raiz import Cliente
from hotel.models_raiz import Venta
from hotel.models_raiz import DetalleVenta
from hotel.models_raiz import Doc_Type


# Register your models here.
admin.site.register(Reservacion)
admin.site.register(Categoria)
admin.site.register(Habitacion)
admin.site.register(DetalleReservacion)
admin.site.register(Forma_de_pago)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Doc_Type)
