"""
Configuración de la aplicación Django para cuentas de usuario.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configuración del módulo de cuentas de usuario y autenticación."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Cuentas de usuario'
