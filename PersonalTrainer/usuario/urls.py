from django.urls import path

from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumno/list', views.alumnos_list, name='alumnos_list'),
    path('alumno/update/<int:pk>', views.alumnos_update, name='alumnos_update'),
    path('alumno/delete/<int:pk>', views.alumnos_delete, name='alumnos_delete'),
    path('alumno/create', views.alumnos_create, name='alumnos_create'),
    path('rutina/main', views.rutina_main, name='rutina_main'),
    path('rutina/list', views.rutina_list, name='rutina_list'),
    path('alumno/rutina', views.rutina_create, name='rutina_create'),
]
