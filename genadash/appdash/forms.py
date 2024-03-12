from django import forms
from .models import Curso, Profesor, Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nombre_curso',
            'comision_curso',
        ]

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            'nombre_profesor',
            'apellido_profesor',
            'email_profesor',
            'especialidad_profesor',
        ]

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre_estudiante',
            'apellido_estudiante',
            'email_estudiante',
        ]
