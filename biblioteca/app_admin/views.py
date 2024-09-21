from django.shortcuts import render


#FUNCIONES DE LA APP ADMIN

#INICIO
#login
def pagina_login(request):
    return render(request, 'app_admin/login.html')
