from django.db import models

class EntradaClinica(models.Model):
    diagnostico = models.CharField(max_length=200)
    tratamiento = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return f"Diagnostico: {self.diagnostico}, Tratamiento: {self.tratamiento}, Fecha: {self.fecha}"