"""
Configuración de los modelos escolares en el panel de administración de Django (Django Admin).
"""

from django.contrib import admin

from .models import Grade, Student, Attendance


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Configuración administrativa para la gestión de grados y secciones escolares.
    """
    list_display = ('name', 'level', 'year', 'is_active')
    list_filter = ('level', 'year', 'is_active')
    search_fields = ('name',)
    ordering = ('level', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Configuración administrativa para la gestión de fichas de estudiantes matriculados.
    """
    list_display = ('student_code', 'last_name', 'first_name', 'grade', 'is_active')
    list_filter = ('grade', 'is_active', 'grade__level')
    search_fields = ('student_code', 'first_name', 'last_name')
    ordering = ('last_name', 'first_name')
    raw_id_fields = ('user',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Configuración administrativa para la auditoría y control de registros diarios de asistencia.
    """
    list_display = ('student', 'date', 'status', 'check_in_time', 'recorded_by', 'created_at')
    list_filter = ('status', 'date', 'student__grade')
    search_fields = ('student__first_name', 'student__last_name', 'student__student_code')
    date_hierarchy = 'date'
    ordering = ('-date', 'student__last_name')
    raw_id_fields = ('student', 'recorded_by')
