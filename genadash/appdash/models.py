from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    comision_curso = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.nombre_curso
    
class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    apellido_estudiante = models.CharField(max_length=100)
    email_estudiante =  models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre_estudiante} {self.apellido_estudiante}"

class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=100)
    apellido_profesor = models.CharField(max_length=100)
    email_profesor = models.EmailField(unique=True)
    especialidad_profesor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_profesor} {self.apellido_profesor}"

