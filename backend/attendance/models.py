"""
Modelos de datos para la gestión escolar: grados, estudiantes y registros diarios de asistencia.
"""

from django.db import models
from django.conf import settings


class Grade(models.Model):
    """
    Representa un grado, curso o sección académica en la institución educativa.
    """

    class Level(models.TextChoices):
        PRIMARIA = 'PRIMARIA', 'Primaria'
        SECUNDARIA = 'SECUNDARIA', 'Secundaria'

    name = models.CharField(max_length=100, verbose_name='Nombre')
    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        verbose_name='Nivel educativo',
    )
    year = models.PositiveIntegerField(verbose_name='Año escolar')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        ordering = ['level', 'name']

    def __str__(self):
        """Representación textual con el nombre, nivel y año escolar."""
        return f'{self.name} - {self.get_level_display()} ({self.year})'


class Student(models.Model):
    """
    Representa a un estudiante formalmente inscrito en la institución escolar.
    """

    student_code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Código de estudiante',
    )
    first_name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, verbose_name='Apellido')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        related_name='students',
        verbose_name='Grado asignado',
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='student_profile',
        verbose_name='Cuenta de usuario vinculada',
    )
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """Representación textual del estudiante con sus apellidos, nombres y código."""
        return f'{self.last_name}, {self.first_name} ({self.student_code})'

    @property
    def full_name(self):
        """Retorna el nombre completo del alumno."""
        return f'{self.first_name} {self.last_name}'


class Attendance(models.Model):
    """
    Registra el control diario de asistencia de un estudiante en una fecha específica.
    Posee una restricción de unicidad para evitar registros duplicados en el mismo día.
    """

    class Status(models.TextChoices):
        PRESENTE = 'PRESENTE', 'Presente'
        AUSENTE = 'AUSENTE', 'Ausente'
        TARDANZA = 'TARDANZA', 'Tardanza'
        JUSTIFICADO = 'JUSTIFICADO', 'Justificado'

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name='Estudiante',
    )
    date = models.DateField(verbose_name='Fecha')
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.PRESENTE,
        verbose_name='Estado de asistencia',
    )
    check_in_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name='Hora de entrada',
    )
    observation = models.TextField(
        blank=True,
        default='',
        verbose_name='Observación',
    )
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='recorded_attendances',
        verbose_name='Docente que registra',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de creación')

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        unique_together = ['student', 'date']
        ordering = ['-date', 'student__last_name']

    def __str__(self):
        """Representación textual con alumno, fecha y estado asentado."""
        return f'{self.student} - {self.date} - {self.get_status_display()}'
