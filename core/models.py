from django.db import models # type: ignore
from datetime import datetime, date

# Create your models here.

class Carrera(models.Model):
    #atributos de la clase
    nombre_Carrera = models.CharField(verbose_name= "Nombre de la carrera", max_length = 50)
    titulo_Carrera = models.CharField(verbose_name= "titulo de la carrera", max_length = 50)
    anios_Estudio = models.IntegerField(verbose_name = "Anios de la carrera" )
    numero_Horas = models.IntegerField(verbose_name= "Horas de la carrera")
    
    def __str__(self):
        return f"{self.nombre_Carrera} - {self.anios_Estudio} anios de estudio"

opciones_estado = [('creado', 'Creado'),('aprobado','Aprobado'),('cancelado','cancelado')]

class Malla(models.Model):
    nombre_malla = models.CharField(verbose_name="Nombre de la malla", max_length=100)
    anioAprobacion = models.IntegerField(verbose_name="Anio de la aprobacion")
    aniosVigencia = models.IntegerField(verbose_name="Anio de vigencia de la Malla")
    estadovigente = models.CharField(verbose_name="Estado", max_length=20, choices=opciones_estado)
    
    #Relaciones entre las clases
    #relacion de uno a muchos
    carrera = models.ForeignKey("Carrera", on_delete= models.CASCADE, verbose_name= "Selecciones una carerra", blank= True, null = True)
    #Relacion de muchos a muchos
    semestres = models.ManyToManyField("Semestre", verbose_name="Agrega los semestres", blank= True, null = True)
    
    def __str__(self):
        return f"{self.nombre_malla} - tiene estado: {self.estadovigente} "
    
class Semestre(models.Model):
    nombreSemestre = models.CharField(verbose_name="Nombre del Semestre", max_length=50)
    numeroSemestre = models.IntegerField(verbose_name= "Numero del semestre")
    
    def __str__(self):
        return f"{self.nombreSemestre} - {self.numeroSemestre} "

opcion_modalidad = [("presencial", "Presencial"), ("Virtual", "Virtual"), ("hibrida", "hibrida")]

class Asignatura(models.Model):
    nombre = models.CharField(verbose_name="Nombre de la Asignatura", max_length=100)
    descripcion = models.TextField(verbose_name="Descripcion de la Asignatura")
    numeroHoras_Docencia= models.IntegerField(verbose_name="Numero Horas de Docencia")
    numeroHoras_Practica = models.IntegerField(verbose_name="Numero de horas de Practica")
    numeroHoras_Autonomo = models.IntegerField(verbose_name="Numero de horas Autonomo")
    creditos = models.IntegerField(verbose_name="Creditos")
    modalidad = models.CharField(verbose_name="Modalidad", max_length=20, choices=opcion_modalidad)
    
    #Relaciones entre las clases
    #relacion de uno a muchos
    semestre = models.ForeignKey("Semestre", on_delete= models.CASCADE, verbose_name= "Agregar el semestre", blank= True, null = True)
    #Relacion de muchos a muchos
    malla = models.ManyToManyField("Malla", verbose_name="Selecciona la Malla", blank= True, null = True)
    
    def __str__(self):
        return f"{self.nombre} - {self.modalidad} "

opcion_estadoCivil = [("Soltero", "Soltero"), ("Casado", "Casado"), ("Divorciado", "Divorciado"), ("viudo", "Viudo")]
opcion_genero = [("masculino", "Masculino"), ("femenino", "Femenino")]
opcion_sexo = [("hombre", "Hombre"), ("mujer","Mujer")] 

class Persona(models.Model):
    nombre = models.CharField(verbose_name="Registra los nombres", max_length=100)
    apellidos = models.CharField(verbose_name="Registra los apellidos", max_length=100)
    cedula_ruc = models.CharField(verbose_name="Ingresa el numero de identificacion", max_length=13)
    telefono = models.CharField(verbose_name="Telefono de casa", max_length=9)
    celular = models.CharField(verbose_name="Numero de celular", max_length=10)
    correo = models.CharField(verbose_name="Ingrese el email", max_length=100)
    fecha_Nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    edad = models.IntegerField(verbose_name="Edad")
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=100, choices=opcion_estadoCivil)
    genero = models.CharField(verbose_name="Seleccione el genero", max_length=100, choices= opcion_genero)
    sexo = models.CharField(verbose_name="Nombre", max_length=100, choices= opcion_sexo)
    
    def _str_(self) -> str:
        return f"{self.nombres} {self.apellidos} - {self.cedula_ruc}"
    
class Estudiante(Persona):
    codigo = models.CharField(verbose_name="Ingresa el codigo", max_length=5)
    correo_institucional = models.EmailField(verbose_name="Correo Institucional", max_length=100)

    def edad_calculada(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_Nacimiento.year
        if hoy.month < self.fecha_Nacimiento.month:
            mes = (hoy.month + 12) - self.fecha_Nacimiento.month
            edad = edad
        else:
            mes = hoy.month - self.fecha_Nacimiento.month
        return f"A: {edad} M: {mes}"

class Administrativo(Persona):
    correo_institucional = models.EmailField(verbose_name="Correo Institucional", max_length=100)
    
class Docente(Persona):
    correo_institucional = models.EmailField(verbose_name="Correo Institucional", max_length=100)
    
#Clase para periodo académico
class PeriodoAcademico(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Periodo académico", max_length=30)
    fecha_inicio = models.DateTimeField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha de Fin")
    activo = models.BooleanField(verbose_name="Avtivo", default=True)
    
    def _str_(self) -> str:
        return f"{self.nombres} - {self.activo}"
    
choice_tipo_pago = [("directo", "Directo"), ("transferencia", "Transferencia"), ("crédito", "Credito")]


class Matricula(models.Model):
    codigo = models.CharField(verbose_name="Ingresa el codigo", max_length=5)
    tipo_Pago = models.CharField(verbose_name="Tipo de Pago", max_length=20, choices=choice_tipo_pago)
    comprobante_Pago = models.ImageField(upload_to="Comprobantes", verbose_name="Comprobante de Pago")
    fecha_Matricula = models.DateField(verbose_name="Fecha de Matricula", default=datetime)
    #Relaciones entre clases
    estudiante = models.ForeignKey("Estudiante", verbose_name="Selecciones el estudiante", on_delete=models.CASCADE)
    carrera = models.ForeignKey("Carrera", verbose_name="Carrera", on_delete=models.CASCADE)
    semestre = models.ForeignKey("Semestre", verbose_name="Semestre", on_delete=models.CASCADE)
    periodo_academico = models.ForeignKey("PeriodoAcademico", verbose_name="PeriodoAcademico", on_delete=models.CASCADE)
    
    def _str_(self) -> str:
        return f"{self.carrera} - {self.estudiante} - {self.semestre} - {self.periodo_academico}"
    


choice_dia_semana = [("lunes", "Lunes"),("martes", "Martes"),("miercoles", "Miercoles"),("jueves", "Jueves"), ("viernes", "Viernes")]
class Horario(models.Model):
    hora_entrada = models.TimeField(verbose_name="Ingrese el horario formato [00:00 - 00:00 ]", null= True, blank=True)
    hora_salida = models.TimeField(verbose_name="Ingrese el horario formato [00:00 - 00:00 ]", null= True, blank=True)
    
    def _str_(self) -> str:
        return f"{self.hora_entrada} - {self.hora_salida}"
class Aula(models.Model):
    nombre = models.CharField(verbose_name="Ingrese el nombre del aula", max_length=100)
    ubicacion = models.CharField(verbose_name="Ingrese el aula", max_length=100) 
    
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    horarioMateria = models.ForeignKey("Horario", on_delete=models.CASCADE, related_name= 'Horario')
    
    def __str__(self):
        return self.nombre, self.horarioMateria
  

        
