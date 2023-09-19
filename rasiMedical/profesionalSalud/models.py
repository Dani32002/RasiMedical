from django.db import models

# Create your models here.
class ProfesionalSalud(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    clave = models.CharField(max_length = 50)
    identificacion = models.CharField(max_length = 50)


    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion