from django.contrib import admin # type: ignore
from.models import Carrera, Semestre, Asignatura, Administrativo, PeriodoAcademico, Matricula, Estudiante, Horario, Aula, Materia
# Register your models here.

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'semestre', 'tipo_Pago')
    search_fields = ('codigo', 'semestre',)
    ordering = ( 'codigo',)
    

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'cedula_ruc', 'celular', 'estado_civil', 'edad_calculada')
    search_fields = ('nombre', 'apellidos', 'cedula_ruc')
    ordering = ('apellidos', 'nombre',)
    list_editable = ('celular', 'estado_civil',)
    fieldsets = (
        ("INFORMACIÓN DEL ESTUDIANTE", {
            'fields':('codigo', 'correo_institucional', )
        }
    ),
    ("DATOS PERSONALES", {
        'fields': ('apellidos', 'nombre', 'cedula_ruc', 'estado_civil', 'fecha_Nacimiento', 'edad', 'genero', 'sexo')
    }
     ),
    ("DATOS DE CONTACTO",{
        'fields': ('celular', 'telefono', 'correo')
    }
     )
    )
admin.site.register(Carrera)
admin.site.register(Semestre)
admin.site.register(Asignatura)
admin.site.register(Administrativo)
admin.site.register(PeriodoAcademico)
admin.site.register(Horario)
admin.site.register(Aula)
admin.site.register(Materia)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Matricula, MatriculaAdmin)


