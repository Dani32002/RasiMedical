from django.db import models

# Create your models here.
class Factura(models.Model):
    numero = models.IntegerField()
    fechaEmision = models.DateField(null = True)
    fechaPago = models.DateField(null = True)
    total = models.IntegerField()