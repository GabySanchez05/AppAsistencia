"""
Configuración del modelo User en el panel de administración de Django (Django Admin).
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Personalización de la interfaz administrativa para el modelo User.
    Permite visualizar, filtrar y editar los campos institucionales como rol,
    teléfono y fotografía de perfil.
    """

    # Columnas que se mostrarán en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')

    # Filtros laterales disponibles
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')

    # Campos por los cuales se puede buscar
    search_fields = ('username', 'first_name', 'last_name', 'email')

    # Ordenamiento por defecto
    ordering = ('username',)

    # Agrupación de campos en el formulario de edición existente
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('role', 'phone', 'profile_image'),
        }),
    )

    # Agrupación de campos en el formulario de creación de nuevo usuario
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Información adicional', {
            'fields': ('role', 'first_name', 'last_name', 'email', 'phone'),
        }),
    )
