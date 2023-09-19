from django.db import models

# Create your models here.
class Elemento(models.Model):
    nombre = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 50)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    #medico = models.ForeignKey(Medico,  on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return "Nombre: " + self.nombre +", Estado: " + self.estado + ", Cantidad: " + self.cantidad + ", Descripcion: " + self.descripcion
