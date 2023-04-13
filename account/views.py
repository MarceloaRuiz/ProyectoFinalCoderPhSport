from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from account.forms import UserRegisterForm
from account.models import Avatar


# Create your views here.
def editar_usuario(request):

    user = request.user
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            user.username = informacion["username"]
            user.email = informacion["email"]
            user.is_staff = informacion["is_staff"]

            try:
                user.avatar.imagen = informacion["imagen"]
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()

            user.save()
            return redirect("home")

    form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff
    })

    context = {
        "form": form,
        "titulo": "Editar usuario",
        "enviar": "Enviar"
    }

    return render(request, "account/form.html", context=context)




def register_account(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("accountLogin")

    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registrar usuario",
        "enviar": "Registrar"
    }
    return render(request, "account/form.html", context=context)


def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user is not None:
                login(request, user)

                return render(request, "account/form.html", context={"mensajes":["Logueado con exito"]})
            else:
                return render(request, "account/form.html", context={"mensajes":["Ingrese los datos correctos"]})
                # return redirect("AppCoderCursos") OTRA FORMA ES REDIRECCIONARLO A OTRA PAGINA.
    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "account/Form.html", context=context)