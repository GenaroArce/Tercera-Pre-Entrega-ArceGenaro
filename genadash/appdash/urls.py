from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('buscar/', buscar, name="buscar"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),

    path('estudiantes/form/', estudianteForm, name='estudiante_form'),  
    path('profesores/form/', profesorForm, name='profesor_form'),  
    path('cursos/form/', cursoForm, name='curso_form'),  

    path('resultados_busqueda/', resultados_busqueda, name="resultados_busqueda"),
]