from django.db import models

# Create your models here.
class Factura(models.Model):
    numero = models.IntegerField()
    fechaEmision = models.DateField(null = True)
    fechaPago = models.DateField(null = True)
    total = models.IntegerField()
    
class EPS(models.Model):
    nombre = models.CharField(max_length = 50)
    nit = models.CharField(max_length = 50)
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", NIT: " + self.nit + " "