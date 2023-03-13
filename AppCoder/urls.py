from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('estudiante/<nombre>/<apellido>', crear_estudiante, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
]