from django.db import models


# Create your models here.
class Factura(models.Model):
    numero = models.IntegerField()
    fechaEmision = models.DateField(null = True)
    paciente = models.ForeignKey('usuario.Paciente',  on_delete=models.CASCADE)
    fechaPago = models.DateField(null = True)
    total = models.IntegerField()

    def __str__(self):
        return "Numero: " + str(self.numero) + ", FechaEmision: " + str(self.fechaEmision) + ", FechaPago: " + str(self.fechaPago) + ", Total:" + str(self.total) + " "
    
class EPS(models.Model):
    nombre = models.CharField(max_length = 50)
    nit = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", NIT: " + self.nit + " "