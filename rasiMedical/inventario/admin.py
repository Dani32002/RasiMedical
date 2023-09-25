from django.contrib import admin

from inventario.models import Dispositivo, Medicamento, Insumo

# Register your models here.

admin.site.register(Dispositivo)
admin.site.register(Medicamento)
admin.site.register(Insumo)