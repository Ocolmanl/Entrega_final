from django import forms

from . import models


class AlumnoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Alumno
        fields = ["dni", "apellido", "nombre", "email", "telefono", "fecha_nacimiento"]

class RutinaCreateForm(forms.ModelForm):
    class Meta:
        model = models.Rutina
        fields = ["instructor","alumno", "nombre", "descripcion", "fecha_inicio", "fecha_fin"]
