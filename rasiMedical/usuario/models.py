from django.db import models

# Definición de clase abstracta del profesional.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    clave = models.CharField(max_length = 50)
    identificacion = models.CharField(max_length = 50)

    class Meta:
        abstract = True

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + " "

#Definición del medico
class Medico(Usuario):
    especialidad = models.CharField(max_length=50)
    licencia = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Especialidad: " + self.especialidad + ", Licencia: " + self.licencia + " "

#Definición del paciente
class Paciente(Usuario):
    numeroDeSeguro = models.CharField(max_length=50)
    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Numero de Seguro: " + self.numeroDeSeguro +  " "

#Definición de la enfermera
class Enfermera(Usuario):
    area = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Area: " + self.area + " "


#Definición de farmaceutico
class Farmaceutico(Usuario):
    #Revisar atributos
    area = models.CharField(max_length=50)
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo + ", Clave: " + self.clave + ", Identificacion: " + self.identificacion + ", Area: " + self.area + " "