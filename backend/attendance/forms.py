"""
Formularios para la administración escolar: grados, estudiantes y registro de asistencia.
"""

from django import forms
from django.utils import timezone

from .models import Grade, Student, Attendance


class GradeForm(forms.ModelForm):
    """
    Formulario para la creación y edición de grados y secciones escolares.
    """

    class Meta:
        model = Grade
        fields = ['name', 'level', 'year', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'level': forms.Select(attrs={'class': 'form-input'}),
            'year': forms.NumberInput(attrs={'class': 'form-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }


class StudentForm(forms.ModelForm):
    """
    Formulario para el registro y modificación de la ficha del estudiante.
    """

    class Meta:
        model = Student
        fields = [
            'student_code', 'first_name', 'last_name',
            'birth_date', 'grade', 'user', 'is_active',
        ]
        widgets = {
            'student_code': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'grade': forms.Select(attrs={'class': 'form-input'}),
            'user': forms.Select(attrs={'class': 'form-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }


class AttendanceForm(forms.ModelForm):
    """
    Formulario para el registro individual de asistencia de un estudiante.
    """

    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status', 'check_in_time', 'observation']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-input'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
            'check_in_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'observation': forms.Textarea(attrs={'class': 'form-input', 'rows': 2}),
        }


class BulkAttendanceForm(forms.Form):
    """
    Formulario dinámico para la toma masiva de asistencia en un grado escolar completo.
    Genera dinámicamente un selector de estado y campo de observación para cada alumno.
    """

    grade = forms.ModelChoiceField(
        queryset=Grade.objects.filter(is_active=True),
        label='Grado escolar',
        widget=forms.Select(attrs={'class': 'form-input', 'id': 'grade-select'}),
    )
    date = forms.DateField(
        label='Fecha lectiva',
        initial=timezone.now,
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
    )

    def __init__(self, *args, **kwargs):
        students = kwargs.pop('students', None)
        super().__init__(*args, **kwargs)

        # Creación dinámica de campos por cada estudiante matriculado
        if students:
            for student in students:
                field_name = f'status_{student.pk}'
                self.fields[field_name] = forms.ChoiceField(
                    choices=Attendance.Status.choices,
                    initial=Attendance.Status.PRESENTE,
                    label=student.full_name,
                    widget=forms.RadioSelect(attrs={'class': 'status-radio'}),
                )
                obs_field_name = f'observation_{student.pk}'
                self.fields[obs_field_name] = forms.CharField(
                    required=False,
                    label='Observación',
                    widget=forms.TextInput(attrs={
                        'class': 'form-input obs-input',
                        'placeholder': 'Observación (opcional)',
                    }),
                )
