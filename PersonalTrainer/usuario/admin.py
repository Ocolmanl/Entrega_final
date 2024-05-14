from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Alumno)
admin.site.register(models.Instructor)
admin.site.register(models.Rutina)