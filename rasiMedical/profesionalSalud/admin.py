from django.contrib import admin

from profesionalSalud.models import Enfermera, Farmaceutico, Medico

# Register your models here.
admin.site.register(Medico)
admin.site.register(Enfermera)
admin.site.register(Farmaceutico)
