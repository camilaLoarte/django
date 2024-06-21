from django.urls import path # type: ignore
from.import views

urlpatterns = [
     #ruta paara presentar la pantalla principal index.html
     path('', views.Index.as_view(), name="pagina-principal"),
     #ruta para ver los estudiantes
     path('lista_estudiantes/', views.Lista_estudiante.as_view(), name="lista_estudiantes"),
     path('crear_estudiante/', views.Agregar_Estudiante.as_view(), name="crear_estudiante"),
     path('eliminar_estudiante/<int:id_estudiante>', views.Eliminar_estudiante.as_view(), name="Eliminar_estudiante"),
     path('actualizar_estudiante/<int:id_estudiante>', views.ActualizarEstudiante.as_view(), name="Actualizar_estudiante"),
    
]
