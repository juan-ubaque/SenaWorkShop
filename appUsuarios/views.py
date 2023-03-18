from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import *

# Create your views here.

#Login
def login (request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email= email, password=password)

        #validamos el usuario
        if user is not None and user.is_active:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'usuarios/login.html', {'alarma': 'usuario o contraseña incorrectos'})
    else:
        return render(request, 'usuarios/login.html')
    

#DESACTIVACION DE USUARIO
@login_required(login_url='/usuarios/login/')
def logout(request):
    auth.logout(request)
    return redirect('login')