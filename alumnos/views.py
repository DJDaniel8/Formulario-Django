from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlumnoForm
from .models import Alumno

def agregar_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')

    else:
        form = AlumnoForm()
    return render(request, 'alumnos/agregar_alumno.html', {'form': form})

def listar_alumnos(request):
    alumnos = Alumno.objects.all()  # Obtener todos los alumnos de la base de datos
    return render(request, 'alumnos/listar_alumnos.html', {'alumnos': alumnos})

def editar_alumno(request, alumno_carnet):
    alumno = get_object_or_404(Alumno, carnet =alumno_carnet)
    print(alumno_carnet)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')  # Redirigir a la página de listado de alumnos
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/editar_alumno.html', {'form': form})

def eliminar_alumno(request, carnet):
    alumno = get_object_or_404(Alumno, carnet=carnet)
    alumno.delete()
    return redirect('listar_alumnos')  # Redirigir a la página de listado de alumnos después de eliminar