from django.shortcuts import render, redirect
from AppCoder.models import Plan_Medicina_Deportiva, Plan_Kinesiologia_Fisioterapia, Plan_Nutricion, Plan_Preparacion_Fisica, Plan_Psicologia_Deportiva
from AppCoder.forms import Plan_Medicina_DeportivaForm, Plan_Kinesiologia_FisioterapiaForm, Plan_NutricionForm, Plan_Preparacion_FisicaForm, Plan_Psicologia_DeportivaForm

""" def busqueda_curso(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }
    return render(request, 'AppCoder/busqueda_curso.html', context=context) """


def editar_plan_medicina_deportiva(request, numero):
    get_plan = Plan_Medicina_Deportiva.objects.get(numero=numero)
    if request.method == "POST":
        mi_formulario = Plan_Medicina_DeportivaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_plan.nombre = informacion['nombre'],
            get_plan.numero = informacion['numero'],
            get_plan.descripcion=informacion['descripcion'],
            get_plan.especialista=informacion['especialista'],
            get_plan.paciente=informacion['paciente'],

            get_plan.save()
            return redirect("Medicina_deportiva")


    context = {
        "numero": numero,
        "form": Plan_Medicina_DeportivaForm(initial={
            "nombre": get_plan.nombre,
            "numero": get_plan.numero
    })
    }
    return render(request, 'AppCoder/editar_plan_medicina_deportiva.html', context=context)


def crear_plan_medicina_deportiva(request):
    if request.method == "POST":
        mi_formulario = Plan_Medicina_DeportivaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            plan_save = Plan_Medicina_Deportiva(
                nombre=informacion['nombre'],
                numero=informacion['numero'],
                descripcion=informacion['descripcion'],
                especialista=informacion['especialista'],
                paciente=informacion['paciente'],
            )
            plan_save.save()
            return redirect("Medicina_deportiva")


    context = {
        "form": Plan_Medicina_DeportivaForm()
    }
    return render(request, 'AppCoder/crear_plan_medicina_deportiva.html', context=context)

def eliminar_plan_medicina_deportiva(request, numero):
    get_plan = Plan_Medicina_Deportiva.objects.get(numero=numero)
    get_plan.delete()

    return redirect("Medicina_deportiva")


def plan_medicina_deportiva(request):

      all_planes = Plan_Medicina_Deportiva.objects.all()
      context = {
        "plan_medicina_deportiva": all_planes,
        "form": Plan_Medicina_DeportivaForm()
      }
      return render(request, "AppCoder/medicina_deportiva.html", context=context)

def plan_nutricion(request):

      all_planes = Plan_Nutricion.objects.all()
      context = {
        "plan_nutricion": all_planes,
        "form": Plan_NutricionForm()
      }
      return render(request, "AppCoder/nutricion.html", context=context)


""" def crear_curso1(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context) """

""" 
def estudiantes(request):
    all_estudiantes = Estudiantes.objects.all()
    context = {
        "estudiantes": all_estudiantes,
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
                apellido=informacion['apellido'],
                email=informacion['email']

            )
            estudiante_save.save()
            return redirect("AppCoderEstudiantes")


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


def editar_estudiante(request, email):
    get_estudiante = Estudiantes.objects.get(email=email)
    if request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_estudiante.nombre=informacion['nombre'],
            get_estudiante.apellido = informacion['apellido'],
            get_estudiante.email = informacion['email'],
            get_estudiante.save()
            return redirect("AppCoderCursos")


    context = {
        "email": email,
       "form": EstudianteForm(initial={
            "nombre": get_estudiante.nombre,
            "apellido": get_estudiante.apellido,
            "email": get_estudiante.email


    })
    }
    return render(request, 'AppCoder/editar_estudiante.html', context=context)

def eliminar_estudiante(request, email):
    get_estudiante = Estudiantes.objects.get(email=email)
    get_estudiante.delete()

    return redirect("AppCoderEstudiantes")


def profesores(request):
    all_profesores = Profesor.objects.all()
    context = {
        "profesores": all_profesores,
        "form": ProfesorForm(),
        "form_busqueda": BusquedaProfesorForm()
    }
    return render(request, "AppCoder/profesores.html", context=context)

def crear_profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor_save = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion'],

            )
            profesor_save.save()
            return redirect("AppCoderProfesores")

    context = {
        "form": ProfesorForm()
    }
    return render(request, 'AppCoder/crear_profesores.html', context=context)

def editar_profesor(request, email):
    get_profesor = Profesor.objects.get(email=email)
    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_profesor.nombre = informacion['nombre'],
            get_profesor.apellido = informacion['apellido'],
            get_profesor.email = informacion['email'],
            get_profesor.profesion = informacion['profesion'],
            get_profesor.save()
            return redirect("AppCoderCursos")


    context = {
        "email": email,
       "form": ProfesorForm(initial={
            "nombre": get_profesor.nombre,
            "apellido": get_profesor.apellido,
            "email": get_profesor.email,
            "profesion": get_profesor.profesion
    })
    }
    return render(request, 'AppCoder/editar_profesor.html', context=context)

def eliminar_profesor(request, email):
    get_profesor = Profesor.objects.get(email=email)
    get_profesor.delete()

    return redirect("AppCoderProfesores")

def busqueda_profesor(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaProfesorForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        profesores_filtrados = Profesor.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "profesores": profesores_filtrados
        }
    return render(request, 'AppCoder/busqueda_profesor.html', context=context) """