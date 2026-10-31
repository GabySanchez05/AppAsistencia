"""
Configuración de la aplicación Django para gestión de asistencia escolar.
"""

from django.apps import AppConfig


class AttendanceConfig(AppConfig):
    """Configuración del módulo de control de asistencias, grados y estudiantes."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'attendance'
    verbose_name = 'Asistencia'
