from django.db import models

# Create your models here.
class Elemento(models.Model):
    nombre = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 200)
    class Meta:
        abstract = True

    def __str__(self):
        return "Nombre: " + self.nombre +", Estado: " + self.estado + ", Descripcion: " + self.descripcion


class Dispositivo(Elemento):
    funcion = models.CharField(max_length = 50)
    def __str__(self):
        return "Nombre: " + self.nombre +", Estado: " + self.estado + ", Descripcion: " + self.descripcion + ", Funcion: " + self.funcion

class Medicamento(Elemento):
    fabricante = models.CharField(max_length = 50)
    concentracion = models.IntegerField()
    administracion = models.CharField(max_length = 50)
    def __str__(self):
        return "Nombre: " + self.nombre +", Estado: " + self.estado + ", Descripcion: " + self.descripcion + ", Fabricante: " + self.fabricante + ", Concentracion: " + str(self.concentracion) + ", Administracion: " + self.administracion

class Insumo(Elemento):
    proposito = models.CharField(max_length = 50)
    unidad = models.CharField(max_length = 50)
    def __str__(self):
        return "Nombre: " + self.nombre +", Estado: " + self.estado + ", Descripcion: " + self.descripcion + ", Proposito: " + self.proposito + ", Unidad: " + self.unidad