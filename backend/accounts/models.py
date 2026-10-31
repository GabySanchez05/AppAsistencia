"""
Modelos de datos para el módulo de cuentas de usuario y control de acceso basado en roles.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser para incorporar
    un sistema de control de acceso basado en roles (RBAC).

    Roles disponibles:
      - ADMIN: Administrador (acceso total a la plataforma y Django Admin).
      - PROFESOR: Docente (control de asistencias y módulos del aula).
      - ESTUDIANTE: Alumno (consulta personal de su ficha escolar y asistencias).
    """

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        PROFESOR = 'PROFESOR', 'Profesor'
        ESTUDIANTE = 'ESTUDIANTE', 'Estudiante'

    # Campo de rol institucional
    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.ESTUDIANTE,
        verbose_name='Rol institucional',
        help_text='Define el nivel de acceso y las vistas permitidas en el sistema.',
    )

    # Teléfono de contacto opcional
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Teléfono',
    )

    # Fotografía de perfil del usuario
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        verbose_name='Imagen de perfil',
    )

    # Administrador personalizado de consultas
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def __str__(self):
        """Representación textual del usuario con su nombre y rol."""
        return f'{self.get_full_name() or self.username} ({self.get_role_display()})'

    @property
    def is_admin(self):
        """Indica si el usuario tiene rol de Administrador."""
        return self.role == self.Role.ADMIN

    @property
    def is_profesor(self):
        """Indica si el usuario tiene rol de Profesor."""
        return self.role == self.Role.PROFESOR

    @property
    def is_gestor(self):
        """Alias para mantener compatibilidad con referencias previas al rol Gestor."""
        return self.is_profesor

    @property
    def is_estudiante(self):
        """Indica si el usuario tiene rol de Estudiante."""
        return self.role == self.Role.ESTUDIANTE

    @property
    def is_usuario(self):
        """Alias para mantener compatibilidad con referencias previas al rol Usuario."""
        return self.is_estudiante
