"""
Configuración de la aplicación Django central (core).
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuración del módulo núcleo con utilidades y comandos administrativos."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Núcleo'
