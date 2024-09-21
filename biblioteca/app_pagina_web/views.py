from django.shortcuts import render


#FUNCIONES DE LA PAGINA WEB

#INICIO
#index
def index(request):
    return render(request, 'app_pagina_web/index.html')
