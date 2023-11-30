from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    clave = models.CharField(max_length = 50)
    identificacion = models.CharField(max_length = 50)

    class Meta:
        abstract = True

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + " "

class Medico(Usuario):
    especialidad = models.CharField(max_length=50)
    licencia = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Especialidad: " + self.especialidad + ", Licencia: " + self.licencia + " "