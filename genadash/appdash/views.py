from django.shortcuts import render, redirect
from .models import *
from .forms import * 

def home(request):
    return render(request, "appdash/index.html") 

def buscar(request):
    return render(request, "appdash/buscar.html") 

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "appdash/cursos.html", contexto) 

def profesores(request):
    return render(request, "appdash/profesores.html") 

def estudiantes(request):
    return render(request, "appdash/estudiantes.html") 

def buscarCursos(request):
    return render(request, "appdash/buscar.html")

def estudianteForm(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = EstudianteForm()
    return render(request, 'appdash/estudiantes.html', {'form': form})

def profesorForm(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProfesorForm()
    return render(request, 'appdash/profesores.html', {'form': form})

def cursoForm(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CursoForm()
    return render(request, 'appdash/cursos.html', {'form': form})

def resultados_busqueda(request):
    if request.method == "GET":
        tipo = request.GET.get('tipo')
        cadena_busqueda = request.GET.get('buscar')
        if tipo == 'curso':
            resultados = Curso.objects.filter(nombre_curso__icontains=cadena_busqueda)
        elif tipo == 'estudiante':
            resultados = Estudiante.objects.filter(nombre_estudiante__icontains=cadena_busqueda)
        elif tipo == 'profesor':
            resultados = Profesor.objects.filter(nombre_profesor__icontains=cadena_busqueda)
        else:
            resultados = None
        contexto = {'resultados': resultados, 'tipo': tipo}
        return render(request, "appdash/resultados_busqueda.html", contexto)
    else:
        return render(request, "appdash/buscar.html")
