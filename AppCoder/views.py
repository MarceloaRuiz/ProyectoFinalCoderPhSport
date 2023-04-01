from django.shortcuts import render, redirect
from .models import Plan_Medicina_Deportiva, Plan_Kinesiologia_Fisioterapia, Plan_Nutricion, Plan_Preparacion_Fisica, Plan_Psicologia_Deportiva
from .forms import Plan_Medicina_DeportivaForm, Plan_Kinesiologia_FisioterapiaForm, Plan_NutricionForm, Plan_Preparacion_FisicaForm, Plan_Psicologia_DeportivaForm

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


def editar_plan_medicina_deportiva(request, id):
    get_plan = Plan_Medicina_Deportiva.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Plan_Medicina_DeportivaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_plan.nombre = informacion['nombre']
            get_plan.numero =  informacion['numero']
            get_plan.descripcion=informacion['descripcion']
            get_plan.especialista=informacion['especialista']
            get_plan.paciente=informacion['paciente']

            get_plan.save()
            return redirect("Medicina_deportiva")


    context = {
        "id": id,
        "form": Plan_Medicina_DeportivaForm(initial={
            "nombre": get_plan.nombre,
            "numero": get_plan.numero,
            "descripcion": get_plan.descripcion,
            "especialista": get_plan.especialista,
            "paciente": get_plan.paciente,
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

def eliminar_plan_medicina_deportiva(request, id):
    get_plan = Plan_Medicina_Deportiva.objects.get(id=id)
    get_plan.delete()

    return redirect("Medicina_deportiva")


def plan_medicina_deportiva(request):

      all_planes = Plan_Medicina_Deportiva.objects.all()
      context = {
        "planes": all_planes,
        "form": Plan_Medicina_DeportivaForm()
      }
      return render(request, "AppCoder/medicina_deportiva.html", context=context)

def plan_nutricion(request):

      all_planes = Plan_Nutricion.objects.all()
      context = {
        "planes": all_planes,
        "form": Plan_NutricionForm()
      }
      return render(request, "AppCoder/nutricion.html", context=context)


def crear_plan_nutricion(request):
    if request.method == "POST":
        mi_formulario = Plan_NutricionForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            plan_save = Plan_Nutricion(
                nombre=informacion['nombre'],
                numero=informacion['numero'],
                descripcion=informacion['descripcion'],
                especialista=informacion['especialista'],
                paciente=informacion['paciente'],
            )
            plan_save.save()
            return redirect("Nutricion")


    context = {
        "form": Plan_NutricionForm()
    }
    return render(request, 'AppCoder/crear_plan_nutricion.html', context=context)


def editar_plan_nutricion(request, id):
    get_plan = Plan_Nutricion.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Plan_NutricionForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_plan.nombre = informacion['nombre']
            get_plan.numero =  informacion['numero']
            get_plan.descripcion=informacion['descripcion']
            get_plan.especialista=informacion['especialista']
            get_plan.paciente=informacion['paciente']

            get_plan.save()
            return redirect("Nutricion")


    context = {
        "id": id,
        "form": Plan_NutricionForm(initial={
            "nombre": get_plan.nombre,
            "numero": get_plan.numero,
            "descripcion": get_plan.descripcion,
            "especialista": get_plan.especialista,
            "paciente": get_plan.paciente,
    })
    }
    return render(request, 'AppCoder/editar_plan_nutricion.html', context=context)


def eliminar_plan_nutricion(request, id):
    get_plan = Plan_Nutricion.objects.get(id=id)
    get_plan.delete()

    return redirect("Nutricion")


def plan_kinesiologia_fisioterapia(request):

      all_planes = Plan_Kinesiologia_Fisioterapia.objects.all()
      context = {
        "planes": all_planes,
        "form": Plan_Kinesiologia_FisioterapiaForm()
      }
      return render(request, "AppCoder/kinesiologia_fisioterapia.html", context=context)


def crear_plan_kinesiologia_fisioterapia(request):
    if request.method == "POST":
        mi_formulario = Plan_Kinesiologia_FisioterapiaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            plan_save = Plan_Kinesiologia_Fisioterapia(
                nombre=informacion['nombre'],
                numero=informacion['numero'],
                descripcion=informacion['descripcion'],
                especialista=informacion['especialista'],
                paciente=informacion['paciente'],
            )
            plan_save.save()
            return redirect("Kinesiologia_Fisioterapia")


    context = {
        "form": Plan_Kinesiologia_FisioterapiaForm()
    }
    return render(request, 'AppCoder/crear_plan_kinesiologia_fisioterapia.html', context=context)


def editar_plan_kinesiologia_fisioterapia(request, id):
    get_plan = Plan_Kinesiologia_Fisioterapia.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Plan_Kinesiologia_FisioterapiaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_plan.nombre = informacion['nombre']
            get_plan.numero =  informacion['numero']
            get_plan.descripcion=informacion['descripcion']
            get_plan.especialista=informacion['especialista']
            get_plan.paciente=informacion['paciente']

            get_plan.save()
            return redirect("Kinesiologia_Fisioterapia")


    context = {
        "id": id,
        "form": Plan_Kinesiologia_FisioterapiaForm(initial={
            "nombre": get_plan.nombre,
            "numero": get_plan.numero,
            "descripcion": get_plan.descripcion,
            "especialista": get_plan.especialista,
            "paciente": get_plan.paciente,
    })
    }
    return render(request, 'AppCoder/editar_plan_kinesiologia_fisioterapia.html', context=context)


def eliminar_plan_kinesiologia_fisioterapia(request, id):
    get_plan = Plan_Kinesiologia_Fisioterapia.objects.get(id=id)
    get_plan.delete()

    return redirect("Kinesiologia_Fisioterapia")