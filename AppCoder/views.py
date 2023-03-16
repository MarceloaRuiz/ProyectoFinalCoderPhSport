from django.shortcuts import render, redirect
from AppCoder.models import Curso, Estudiantes
from AppCoder.forms import CursoForm, BusquedaCursoForm, EstudianteForm, ProfesorForm, BusquedaEstudianteForm, BusquedaProfesorForm

def busqueda_curso(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }
    return render(request, 'AppCoder/busqueda_curso.html', context=context)

def editar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_curso.nombre=informacion['nombre'],
            get_curso.camada=informacion['camada']

            get_curso.save()
            return redirect("AppCoderCursos")


    context = {
        "camada": camada,
        "form": CursoForm(initial={
            "nombre": get_curso.nombre,
            "camada": get_curso.camada
    })
    }
    return render(request, 'AppCoder/editar curso.html', context=context)
def crear_curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            curso_save.save()
            return redirect("AppCoderCursos")


    context = {
        "form": CursoForm()
    }
    return render(request, 'AppCoder/crear curso.html', context=context)

def eliminar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)
    get_curso.delete()

    return redirect("AppCoderCursos")
def cursos(request):

      all_cursos = Curso.objects.all()
      context = {
        "cursos": all_cursos,
        "form": CursoForm(),
        "form_busqueda": BusquedaCursoForm()
      }
      return render(request, "AppCoder/cursos.html", context=context)


def crear_curso1(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)


def estudiantes(request):
    all_estudiantes = Estudiantes.objects.all()
    context = {
        "cursos": all_estudiantes,
        "form": EstudianteForm(),
        "form_busqueda": BusquedaEstudianteForm()
    }
    return render(request, "AppCoder/estudiantes.html", context=context)

def crear_estudiante(request):
    if request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante_save = Estudiantes(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            estudiante_save.save()
            return redirect("AppCoderCursos")


    context = {
        "form": EstudianteForm()
    }
    return render(request, 'AppCoder/crear_estudiante.html', context=context)

def busqueda_estudiante(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaEstudianteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        estudiantes_filtrados = Estudiantes.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "estudiantes": estudiantes_filtrados
        }
    return render(request, 'AppCoder/busqueda_estudiante.html', context=context)



def crear_estudiante(request, nombre, apellido, email):
    save_estudiante = Estudiantes(nombre=nombre, apellido=apellido, email=email)
    save_estudiante.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_estudiante.html", context)


def profesores(request):
    all_profesores = profesores.objects.all()
    context = {
        "cursos": all_profesores,
        "form": ProfesorForm(),
        "form_busqueda": BusquedaProfesorForm()
    }
    return render(request, "AppCoder/profesores.html", context=context)

def crear_profesores(request, nombre, apellido, email, profesion):
    save_profesores = profesores(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    save_profesores.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_profesores.html", context)

def busqueda_profesor(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaProfesorForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        profesores_filtrados = profesores.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "profesores": profesores_filtrados
        }
    return render(request, 'AppCoder/busqueda_profesor.html', context=context)

