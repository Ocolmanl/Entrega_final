from django.shortcuts import render, redirect
from usuario.forms import AlumnoCretaForm
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
        form = AlumnoCretaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:index")
    else:  # GET
        form = AlumnoCretaForm()
    return render(request, "usuario/create_alumnos.html", {"form": form})
