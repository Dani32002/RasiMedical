from django.contrib import admin
from .models import Medico, Enfermera, Farmaceutico


# Register your models here.
admin.site.register(Medico)
admin.site.register(Enfermera)
admin.site.register(Farmaceutico)