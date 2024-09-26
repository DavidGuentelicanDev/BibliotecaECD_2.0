from django.shortcuts import render, redirect
#login logout y permisos
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse


#FUNCIONES DE LA APP ADMIN

#INICIO
#login
def pagina_login(request):
    return render(request, 'app_admin/login.html')

#funcion para el login admin
def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('correoAdmin')
        password = request.POST.get('contrasenaAdmin')
        #autentificar usando username y password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'No tienes permisos para acceder a este módulo'
                })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Usuario y/o Contraseña inválidos. Vuelve a ingresar con credenciales registradas. Si no tienes usuario, comunícate con tu jefatura para solicitar credenciales'
            })

#pagina home
@login_required
def home(request):
    return render(request, 'app_admin/home.html')

#funcion de logout
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
