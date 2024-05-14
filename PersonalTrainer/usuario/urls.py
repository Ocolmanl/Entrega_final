from django.urls import path

from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/list', views.alumnos_list, name='alumnos_list'),
    path('alumnos/create', views.alumnos_create, name='alumnos_create')
    
]
