from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('cursos/<nombre>/<camada>', crear_curso,name="AppCoderCursos"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
]
