from django import forms  # type: ignore
from .models import *

class EstudianteForms(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        labels = {
            'apellidos': 'Ingrese los Apellidos',
            'nombres': 'Ingrese los Nombres',
            'cedula_ruc': 'Cedula o Ruc',
            'correo': 'Ingrese el correo',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'genero': 'Genero',
            'estado_civil': 'Estado Civil',
            'correo_institucional': 'Registre el correo Institucional'
        }