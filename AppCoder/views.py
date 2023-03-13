from django.shortcuts import render
from AppCoder.models import Curso, Estudiantes


def cursos(request):
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "AppCoder/cursos.html", context=context)


def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)


def estudiantes(request):
    all_estudiantes = Estudiantes.objects.all()
    context = {
        "cursos": all_estudiantes
    }
    return render(request, "AppCoder/estudiantes.html", context=context)


def crear_estudiante(request, nombre, apellido, email):
    save_estudiante = Estudiantes(nombre=nombre, apellido=apellido, email=email)
    save_estudiante.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_estudiante.html", context)


def profesores(request):
    return render(request, "base.html")
