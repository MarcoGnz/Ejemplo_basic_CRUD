from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Ejemplo
from .forms import EjemploForm

def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")


def crear_ejemplo(request):
    if request.method == 'POST':
        form = EjemploForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ejemplos')
    else:
        form = EjemploForm()
    return render(request, 'basic_CRUD/crear_ejemplo.html', {'form': form})

def lista_ejemplos(request):
    ejemplos = Ejemplo.objects.all()
    return render(request, 'basic_CRUD/lista_ejemplos.html', {'ejemplos': ejemplos})

def editar_ejemplo(request, id):
    ejemplo = get_object_or_404(Ejemplo, id=id)
    if request.method == 'POST':
        form = EjemploForm(request.POST, instance=ejemplo)
        if form.is_valid():
            form.save()
            return redirect('lista_ejemplos')
    else:
        form = EjemploForm(instance=ejemplo)
    return render(request, 'basic_CRUD/editar_ejemplo.html', {'form': form, 'ejemplo': ejemplo})

def eliminar_ejemplo(request, id):
    ejemplo = get_object_or_404(Ejemplo, id=id)
    if request.method == 'POST':
        ejemplo.delete()
        return redirect('lista_ejemplos')
    return render(request, 'basic_CRUD/eliminar_ejemplo.html', {'ejemplo': ejemplo})