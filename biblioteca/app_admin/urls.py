from django.urls import path
from . import views

urlpatterns = [
    #inicio/login admin
    path('', views.pagina_login, name='login'), #pagina login admin
    path('login_admin/', views.login_admin, name='admin_login'), #funcion para el login admin
    path('home/', views.home, name='home_page'), #home del admin
    path('cierre_sesion/', views.cerrar_sesion, name='logout'), #funcion para logout
]
