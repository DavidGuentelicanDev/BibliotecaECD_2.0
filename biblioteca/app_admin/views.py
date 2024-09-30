from django.shortcuts import render, redirect
#login logout y permisos
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

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

#funcion para permisos staff solamente
def staff_requerido(user):
    return user.is_staff

#funcion para permisos admin staff
def admin_requerido(user):
    return user.rol == 1

#funcion para permisos admin y biliotecario staff
def bibliotecario_requerido(user):
    return user.rol == 1 or user.rol == 2

#pagina que redirige a mensaje sin permisos
def sin_acceso(request):
    return render(request, 'app_admin/sin_permisos.html')

#pagina home
@login_required(login_url='/app_admin/sin_acceso/')
@user_passes_test(staff_requerido, login_url='/app_admin/sin_acceso/')
def home(request):
    return render(request, 'app_admin/home.html')

#funcion de logout
@login_required(login_url='/app_admin/sin_acceso/')
@user_passes_test(staff_requerido, login_url='/app_admin/sin_acceso/')
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
