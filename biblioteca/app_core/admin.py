from django.contrib import admin
from .models import Pais, Editorial, Libro, Autor, AutorPorLibro, Usuario, Reserva, DetalleReserva
from django.contrib.auth.admin import UserAdmin


admin.site.register(Pais)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(AutorPorLibro)
admin.site.register(Reserva)
admin.site.register(DetalleReserva)

class CustomUsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'rut', 'telefono', 'rol')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'rut', 'telefono', 'rol'),
        }),
    )
    list_display = ('username', 'first_name', 'last_name', 'rol', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'rol')
    ordering = ('username',)

admin.site.register(Usuario, CustomUsuarioAdmin)
