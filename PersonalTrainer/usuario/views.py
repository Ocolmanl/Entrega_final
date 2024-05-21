from django.shortcuts import render, redirect, get_object_or_404
from usuario.forms import AlumnoCreateForm, RutinaCreateForm
from usuario.models import Alumno, Rutina

# Create your views here.
def index(request):
    
    return render(request, 'usuario/index.html')

def alumnos_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Alumno.objects.filter(apellido__icontains=busqueda)
    else:
        consulta = Alumno.objects.all()
    contexto = {"alumnos": consulta}
    return render(request, "usuario/alumnos_list.html", contexto)

def alumnos_update(request, pk: int):
    consulta = get_object_or_404(Alumno, id=pk)
    if request.method == "POST":
        form = AlumnoCreateForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("usuario:alumnos_list")
    else:  # GET
        form = AlumnoCreateForm(instance=consulta)
    return render(request, "usuario/alumnos_form.html", {"form": form})

def alumnos_delete(request, pk: int):
    consulta = Alumno.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("usuario:alumnos_list")
    return render(request, "usuario/confirm_delete_alumno.html", {"object": consulta})

def alumnos_create(request):
    if request.method == "POST":
        form = AlumnoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:index")
    else:  # GET
        form = AlumnoCreateForm()
    return render(request, "usuario/alumnos_form.html", {"form": form})

def rutina_create(request):
    if request.method == "POST":
        form = RutinaCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:index")
    else:  # GET
        form = RutinaCreateForm()
    return render(request, "usuario/rutina_create.html", {"form": form})

def rutina_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Rutina.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Rutina.objects.all()
    contexto = {"rutinas": consulta}
    return render(request, "usuario/rutina_list.html", contexto)

def rutina_main(request):
    return render(request, 'usuario/rutina_main.html')

def rutina_update(request, pk: int):
    consulta = get_object_or_404(Rutina, id=pk)
    if request.method == "POST":
        form = RutinaCreateForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("usuario:rutina_list")
    else:  # GET
        form = RutinaCreateForm(instance=consulta)
    return render(request, "usuario/rutina_form.html", {"form": form})

def rutina_delete(request, pk: int):
    consulta = Rutina.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("usuario:rutina_list")
    return render(request, "usuario/confirm_delete_rutina.html", {"object": consulta})