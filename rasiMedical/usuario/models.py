from django.db import models

# Definición de clase abstracta del profesional.
class ProfesionalSalud(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    clave = models.CharField(max_length = 50)
    identificacion = models.CharField(max_length = 50)

    class Meta:
        abstract = True

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion

#Definición del medico
class Medico(ProfesionalSalud):
    especialidad = models.CharField(max_length=50)
    licencia = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Especialidad: " + self.especialidad + ", Licencia: " + self.licencia


#Definición de la enfermera
class Enfermera(ProfesionalSalud):
    area = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Area: " + self.area


#Definición de farmaceutico
class Farmaceutico(ProfesionalSalud):
    #Revisar atributos
    area = models.CharField(max_length=50)
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Area: " + self.area