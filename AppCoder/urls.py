from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('cursos/crear', crear_curso, name="AppCoderCrearCursos"),
    path('cursos/editar/<camada>', editar_curso, name="AppCoderEditarCursos"),
    path('cursos/eliminar/<camada>', eliminar_curso, name="AppCoderEliminarCursos"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('buscar_estudiante', busqueda_estudiante, name="AppCoderBuscarEstudiantes"),
    path('estudiantes/crear', crear_estudiante, name="AppCoderCrearEstudiantes"),
    path('estudiantes/editar', editar_estudiante, name="AppCoderEditarEstudiantes"),
    path('estudiante/eliminar', eliminar_estudiante, name="AppCoderEliminarEstudiantes"),
    path('profesores', Profesores, name="AppCoderProfesores"),
    path('profesores/crear', crear_profesores, name="AppCoderCrearProfesores"),
    path('buscar_prefesores', busqueda_profesor, name="AppCoderBuscarProfesores"),
    path('profesores/editar', editar_profesor, name="AppCoderEditarProfesores"),
    path('profesor/eliminar', eliminar_profesor, name="AppCoderEliminarProfesores"),
]