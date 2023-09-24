from django.db import models

from profesionalSalud.models import Medico

# Create your models here.
class Elemento(models.Model):
    nombre = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 50)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    medico = models.ForeignKey(Medico,  on_delete=models.SET_NULL, null = True)
    class Meta:
        abstract = True

    def __str__(self):
        return "Nombre: " + self.nombre +", Estado: " + self.estado + ", Cantidad: " + str(self.cantidad) + ", Descripcion: " + self.descripcion


class Dispositivo(models.Model):
    funcion = models.CharField(max_length = 50)

class Medicamento(models.Model):
    fabricante = models.CharField(max_length = 50)
    concentracion = models.IntegerField()
    administracion = models.CharField(max_length = 50)

class Insumo(models.Model):
    proposito = models.CharField(max_length = 50)
    unidad = models.CharField(max_length = 50)