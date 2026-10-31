"""
Enrutamiento URL para la aplicación de asistencia escolar (attendance).
"""

from django.urls import path
from accounts.views import HomeView
from . import views

app_name = 'attendance'

urlpatterns = [
    # Redirección inteligente del inicio según rol
    path('', HomeView.as_view(), name='home'),

    # Panel del Administrador
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),

    # Panel Docente para profesores
    path('profesor-dashboard/', views.ProfesorDashboardView.as_view(), name='profesor_dashboard'),

    # Portal del Estudiante
    path('estudiante-dashboard/', views.EstudianteDashboardView.as_view(), name='estudiante_dashboard'),

    # Portal informativo público para visitantes
    path('info/', views.PublicInfoView.as_view(), name='public_info'),

    # Rutas alias para compatibilidad y retrocompatibilidad
    path('dashboard/', HomeView.as_view(), name='dashboard'),
    path('my-attendance/', HomeView.as_view(), name='my_attendance'),
]
