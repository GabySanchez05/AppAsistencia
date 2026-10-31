"""
Rutas URL para la aplicación de autenticación y cuentas (accounts).
"""

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Inicio de sesión
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # Cierre de sesión
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # Registro de nuevos usuarios
    path('register/', views.RegisterView.as_view(), name='register'),

    # Actualización del perfil de usuario autenticado
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
