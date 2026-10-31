"""
Formularios para autenticación, registro de nuevos usuarios y actualización de perfiles.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class LoginForm(AuthenticationForm):
    """
    Formulario de inicio de sesión con estilos visuales escolares aplicados
    a los campos de usuario y contraseña.
    """

    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nombre de usuario',
            'autofocus': True,
        }),
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Contraseña',
        }),
    )


class RegisterForm(UserCreationForm):
    """
    Formulario para el registro de nuevos usuarios en el sistema.
    - El público general puede auto-registrarse como Estudiante o Profesor.
    - Si la cuenta autenticada que registra es Administrador, tiene la potestad
      de crear usuarios con cualquier rol institucional (incluyendo Admin).
    """

    first_name = forms.CharField(
        label='Nombre',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Juan'}),
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Pérez'}),
    )
    email = forms.EmailField(
        label='Correo electrónico',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'correo@ejemplo.com'}),
    )
    role = forms.ChoiceField(
        label='Tipo de Usuario',
        choices=[
            (User.Role.ESTUDIANTE, 'Estudiante'),
            (User.Role.PROFESOR, 'Profesor'),
        ],
        initial=User.Role.ESTUDIANTE,
        widget=forms.Select(attrs={'class': 'form-input'}),
        help_text='Selecciona si eres Estudiante o Profesor.',
    )

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'role', 'password1', 'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre de usuario'}),
        }

    def __init__(self, *args, is_admin=False, **kwargs):
        super().__init__(*args, **kwargs)
        if is_admin:
            # Si el usuario que registra es administrador, puede crear cualquier rol
            self.fields['role'].choices = User.Role.choices
        else:
            # El registro público general solo permite Estudiante o Profesor
            self.fields['role'].choices = [
                (User.Role.ESTUDIANTE, 'Estudiante'),
                (User.Role.PROFESOR, 'Profesor'),
            ]


class UserProfileForm(forms.ModelForm):
    """
    Formulario que permite a los usuarios autenticados editar y actualizar
    sus datos personales de contacto e imagen de perfil.
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'profile_image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+58 412 1234567'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-input'}),
        }
