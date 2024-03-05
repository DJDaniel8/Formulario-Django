from django.db import models

class Alumno(models.Model):
    carnet = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoElectronico = models.EmailField()
    fechaNacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
