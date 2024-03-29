from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlumnoForm
from .models import Alumno
from datetime import datetime

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

def cantidad_alumnos_por_edad(request):
    # Calcular la edad actual de los alumnos y categorizarlos
    now = datetime.now()
    alumnos = Alumno.objects.all()
    edades = {}

    for alumno in alumnos:
        edad = now.year - alumno.fechaNacimiento.year - ((now.month, now.day) < (alumno.fechaNacimiento.month, alumno.fechaNacimiento.day))
        # Categorizar por rango de edad
        if edad in edades:
            edades[edad] += 1
        else:
            edades[edad] = 1

    # Ordenar las edades por clave (edad)
    edades = dict(sorted(edades.items()))

    # Pasar los datos a la plantilla HTML
    return render(request, 'alumnos/cantidad_alumnos_por_edad.html', {'edades': edades})