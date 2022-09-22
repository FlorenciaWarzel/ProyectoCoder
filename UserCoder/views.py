from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.

# Vistas "Registro"
from UserCoder.forms import UserRegisterForm
from UserCoder.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            contrasenia = data.get('password')
            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, f'Bienvenido/a {user}!')
            else:
                messages.info(request, 'inicio de sesion fallido!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('AppInicio')

    contexto = {
        'form': AuthenticationForm()
    }
    return render(request, 'UserCoder/login.html', contexto)


def registro(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            user= form.save()
            avatar = Avatar(user=user, imagen=form.cleaned_data.get('imagen'))
            avatar.save()

            messages.info(request, 'El usuario fue correctamente creado.')
        else:
            messages.info(request, 'El usuario no pudo ser registrado. Inténtalo nuevamente.')

        return redirect('AppInicio')

    context = {

        'form': UserRegisterForm()

    }
    return render(request, "UserCoder/registro.html", context)

# Vistas Logout

