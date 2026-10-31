"""
Administrador personalizado de consultas (Manager) para el modelo User.
"""

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Manager personalizado para el modelo User donde el nombre de usuario (username)
    es el identificador único requerido para la autenticación en el sistema.
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Crea y guarda un usuario regular con los datos y contraseña proporcionados.
        """
        if not username:
            raise ValueError('El nombre de usuario es obligatorio.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con permisos administrativos totales
        (is_staff=True, is_superuser=True y rol ADMIN).
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
