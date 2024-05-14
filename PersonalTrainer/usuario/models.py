from django.db import models

# Create your models here.
class Alumno(models.Model):
    dni = models.IntegerField()
    apellido = models.CharField(max_length=100) 
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.apellido
    
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class Instructor(models.Model):
    apellido = models.CharField(max_length=100) 
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.apellido
    
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'


class Rutina(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name="Instructor asignado")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno asignado")
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la rutina")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'
