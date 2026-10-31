"""
Vistas de presentación del sistema escolar organizadas según los roles institucionales.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from core.mixins import AdminRequiredMixin, ProfesorRequiredMixin


class AdminDashboardView(AdminRequiredMixin, TemplateView):
    """
    Vista del Panel de Administración.
    Restringida exclusivamente a usuarios con rol de Administrador.
    Proporciona accesos centralizados a Django Admin, creación de cuentas y configuración.
    """
    template_name = 'attendance/admin_dashboard.html'


class ProfesorDashboardView(ProfesorRequiredMixin, TemplateView):
    """
    Vista del Panel Docente.
    Accesible para el cuerpo docente y personal administrativo.
    Estructura el espacio de trabajo para el control de asistencia y seguimiento de cursos.
    """
    template_name = 'attendance/profesor_dashboard.html'


class EstudianteDashboardView(LoginRequiredMixin, TemplateView):
    """
    Vista del Portal del Estudiante.
    Accesible para estudiantes autenticados en la plataforma.
    Presenta la ficha personal del alumno y la consulta de su historial de asistencias.
    """
    template_name = 'attendance/estudiante_dashboard.html'


class PublicInfoView(TemplateView):
    """
    Vista informativa abierta al público general y visitantes no autenticados.
    Presenta la misión del sistema de asistencia, resumen de roles y accesos de registro e ingreso.
    """
    template_name = 'public/info.html'
