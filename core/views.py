from django.shortcuts import render # type: ignore
from django.views import View  # type: ignore
from .models import Estudiante
from .forms import EstudianteForms
from django.http import HttpResponseRedirect 
# Create your views here.

def index(request):
    return render(request, 'principal/index.html')

class Index(View):
    def get(self, request):
        return render(request, 'principal/index.html')
    
class Lista_estudiante(View):
    def get(self, request):
        #orm de django - orm es el motor de gestion de consultas de base de datos
        lista_estudiante= Estudiante.objects.all()
        print(lista_estudiante)
        return render(request, 'estudiantes/lista_estudiantes.html', {
           'lista_estudiantes': lista_estudiante, 

        })
class Agregar_Estudiante(View):
    def get(self, request):
        form = EstudianteForms()
        return render(request, 'estudiantes/agregarestudiante.html', {
           'form': form
       }) 
    
    def post(self, request):
        form = EstudianteForms(request.POST or None)
        print(form)
        if form.is_valid():
            nombres = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            cedula_ruc = form.cleaned_data['cedula_ruc']
            telefono = form.cleaned_data['telefono']
            celular = form.cleaned_data['celular']
            correo = form.cleaned_data['correo']
            fecha_Nacimiento = form.cleaned_data['fecha_Nacimiento']
            edad = form.cleaned_data['edad']
            estado_civil = form.cleaned_data['estado_civil']
            genero = form.cleaned_data['genero']
            sexo = form.cleaned_data['sexo']
            codigo = form.cleaned_data['codigo']
            correo_institucional = form.cleaned_data['correo_institucional']
            
            estudiante = Estudiante(
                nombre = nombres,
                apellidos = apellidos,
                cedula_ruc = cedula_ruc,
                telefono = telefono,
                celular = celular,
                correo = correo,
                fecha_Nacimiento = fecha_Nacimiento,
                edad = edad,
                estado_civil = estado_civil,
                genero = genero,
                sexo = sexo,
                codigo = codigo,
                correo_institucional = correo_institucional
            )
            estudiante.save()
            form = EstudianteForms()
            return HttpResponseRedirect('/core/lista_estudiantes')
        else:
            return render(request, 'estudiante/crear_estudiante.html',{'form': form})
        
class Eliminar_estudiante(View):
    def get(self, request, id_estudiante):
        estudiante = Estudiante.objects.get(id = id_estudiante)
        if estudiante:
            estudiante.delete()
            return HttpResponseRedirect('/core/lista_estudiantes')
        else:
            return 'error'
        
class ActualizarEstudiante(View):
    def get(self, request, id_estudiante):
        estudiante = Estudiante.objects.get(id = id_estudiante)
        form = EstudianteForms(instance=estudiante)
        return render(request, 'estudiantes/agregarestudiante.html', {
           'form': form
       })
    
    def post(self, request, id_estudiante):
        form = EstudianteForms(request.POST or None)
        print(form)
        if form.is_valid():
            nombres = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            cedula_ruc = form.cleaned_data['cedula_ruc']
            telefono = form.cleaned_data['telefono']
            celular = form.cleaned_data['celular']
            correo = form.cleaned_data['correo']
            fecha_Nacimiento = form.cleaned_data['fecha_Nacimiento']
            edad = form.cleaned_data['edad']
            estado_civil = form.cleaned_data['estado_civil']
            genero = form.cleaned_data['genero']
            sexo = form.cleaned_data['sexo']
            codigo = form.cleaned_data['codigo']
            correo_institucional = form.cleaned_data['correo_institucional']
           
            estudiante = Estudiante.objects.get(id = id_estudiante) 
            estudiante.nombre = nombres
            estudiante.apellidos = apellidos
            estudiante.cedula_ruc = cedula_ruc
            estudiante.telefono = telefono
            estudiante.celular = celular
            estudiante.correo = correo
            estudiante.fecha_Nacimiento = fecha_Nacimiento
            estudiante.edad = edad
            estudiante.estado_civil = estado_civil
            estudiante.genero = genero
            estudiante.sexo = sexo
            estudiante.codigo = codigo
            estudiante.correo_institucional = correo_institucional
            
            estudiante.save()
            form = EstudianteForms()
            return HttpResponseRedirect('/core/lista_estudiantes')
        else:
            return render(request, 'estudiante/crear_estudiante.html',{'form': form})
        
class Lista_Docentes(View):
    def get(self, request):
        #orm de django - orm es el motor de gestion de consultas de base de datos
        lista_Docentes= Estudiante.objects.all()
        print(lista_Docentes)
        return render(request, 'estudiantes/lista_estudiantes.html', {
           'lista_estudiantes': lista_Docentes, 

        })