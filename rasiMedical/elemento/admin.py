from django.contrib import admin

from elemento.models import Dispositivo, Insumo, Medicamento

# Register your models here.
admin.site.register(Dispositivo)
admin.site.register(Medicamento)
admin.site.register(Insumo)