from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('cursos/crear', crear_curso, name="AppCoderCrearCursos"),
    path('cursos/editar/<camada>', editar_curso, name="AppCoderEditarCursos"),
    path('cursos/eliminar/<camada>', eliminar_curso, name="AppCoderEliminarCursos"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
    path('curso/<nombre>/<camada>', crear_curso1, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('estudiante/<nombre>/<apellido>', crear_estudiante, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
]