from django import forms

from . import models


class AlumnoCretaForm(forms.ModelForm):
    class Meta:
        model = models.Alumno
        fields = ["dni", "apellido", "nombre", "email", "telefono", "fecha_nacimiento"]
