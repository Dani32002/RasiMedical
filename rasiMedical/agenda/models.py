from django.db import models


# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    completada = models.BooleanField()
    medicoCita = models.ForeignKey('usuario.Medico',  on_delete=models.SET_NULL)
    paciente = models.ForeignKey('usuario.Paciente',  on_delete=models.CASCADE)
    factura = models.ForeignKey('administrativo.Factura',  on_delete=models.CASCADE, null= True)

