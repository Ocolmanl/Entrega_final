from django.shortcuts import render, redirect
from usuario.forms import AlumnoCreateForm, RutinaCreateForm
from usuario.models import Alumno

# Create your views here.
def index(request):
    
    return render(request, 'usuario/index.html')

def alumnos_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Alumno.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Alumno.objects.all()
    contexto = {"alumnos": consulta}
    return render(request, "usuario/consulta_alumnos.html", contexto)

def alumnos_create(request):
    if request.method == "POST":
        form = AlumnoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:index")
    else:  # GET
        form = AlumnoCreateForm()
    return render(request, "usuario/create_alumnos.html", {"form": form})

def alumnos_delete(request, pk: int):
    consulta = Alumno.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("usuario:consulta_alumnos.html")
    return render(request, "usuario/confirm_delete_alumno.html", {"object": consulta})

def rutina_create(request):
    if request.method == "POST":
        form = RutinaCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:index")
    else:  # GET
        form = RutinaCreateForm()
    return render(request, "usuario/rutina_alumno.html", {"form": form})