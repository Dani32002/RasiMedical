from django.contrib import admin
from .models import Medico, Enfermera, Farmaceutico, Administrador


# Register your models here.
admin.site.register(Medico)
admin.site.register(Enfermera)
admin.site.register(Farmaceutico)
admin.site.register(Administrador)