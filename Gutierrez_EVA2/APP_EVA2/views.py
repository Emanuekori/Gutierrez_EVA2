from django.shortcuts import render, redirect
from .models import Inscripcion
from .forms import InscripcionForm

def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'listar_inscripciones.html', {'inscripciones': inscripciones})

def agregar_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'agregar_inscripcion.html', {'form': form})

def modificar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id) 
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'agregar_inscripcion.html', {'form': form})

def eliminar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)  
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('listar_inscripciones')
    return render(request, 'confirmar_eliminacion.html', {'inscripcion': inscripcion})
