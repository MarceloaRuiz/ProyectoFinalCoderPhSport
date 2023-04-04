from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('medicina_deportiva/', plan_medicina_deportiva, name="Medicina_deportiva"),
    path('medicina_deportiva/crear', crear_plan_medicina_deportiva, name="crear_plan_medicina_deportiva"),
    path('medicina_deportiva/editar/<int:id>/', editar_plan_medicina_deportiva, name="editar_plan_medicina_deportiva"),
    path('medicina_deportiva/eliminar/<int:id>', eliminar_plan_medicina_deportiva, name="eliminar_plan_medicina_deportiva"),

    path('nutricion/', plan_nutricion, name="Nutricion"),
    path('nutricion/crear', crear_plan_nutricion, name="crear_plan_nutricion"),
    path('nutricion/editar/<int:id>/', editar_plan_nutricion, name="editar_plan_nutricion"),
    path('nutricion/eliminar/<int:id>', eliminar_plan_nutricion, name="eliminar_plan_nutricion"),

    path('kinesiologia_fisioterapia/', plan_kinesiologia_fisioterapia, name="Kinesiologia_Fisioterapia"),
    path('kinesiologia_fisioterapia/crear', crear_plan_kinesiologia_fisioterapia, name="crear_plan_kinesiologia_fisioterapia"),
    path('kinesiologia_fisioterapia/editar/<int:id>/', editar_plan_kinesiologia_fisioterapia, name="editar_plan_kinesiologia_fisioterapia"),
    path('kinesiologia_fisioterapia/eliminar/<int:id>', eliminar_plan_kinesiologia_fisioterapia, name="eliminar_plan_kinesiologia_fisioterapia"),

    path('preparacion_fisica/', plan_preparacion_fisica, name="Preparacion_Fisica"),
    path('preparacion_fisica/crear', crear_plan_preparacion_fisica, name="crear_plan_preparacion_fisica"),
    path('preparacion_fisica/editar/<int:id>/', editar_plan_preparacion_fisica, name="editar_plan_preparacion_fisica"),
    path('preparacion_fisica/eliminar/<int:id>', eliminar_plan_preparacion_fisica, name="eliminar_plan_preparacion_fisica"),

    path('psicologia_deportiva/', plan_psicologia_deportiva, name="Psicologia_Deportiva"),
    path('psicologia_deportiva/crear', crear_plan_psicologia_deportiva, name="crear_plan_psicologia_deportiva"),
    path('psicologia_deportiva/editar/<int:id>/', editar_plan_psicologia_deportiva, name="editar_plan_psicologia_deportiva"),
    path('psicologia_deportiva/eliminar/<int:id>', eliminar_plan_psicologia_deportiva, name="eliminar_plan_psicologia_deportiva"),

    path('acerca_de_nosotros/', about, name="acerca_de_nosotros"),

]
