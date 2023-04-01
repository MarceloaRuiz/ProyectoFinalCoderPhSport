from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('medicina_deportiva/', plan_medicina_deportiva, name="Medicina_deportiva"),
    path('medicina_deportiva/crear', crear_plan_medicina_deportiva, name="crear_plan_medicina_deportiva"),
    path('medicina_deportiva/editar/<numero>', editar_plan_medicina_deportiva, name="editar_plan_medicina_deportiva"),
    #path('medicina_deportiva/eliminar/<numero>', eliminar_curso, name="AppCoderEliminarCursos"),

    path('nutricion/', plan_nutricion, name="Nutricion"),
]