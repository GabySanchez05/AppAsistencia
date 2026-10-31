"""
Controladores y vistas basadas en clases para autenticación, gestión de sesiones y perfiles.
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

from .forms import LoginForm, RegisterForm, UserProfileForm
from .models import User


class HomeView(TemplateView):
    """
    Vista de enrutamiento principal (raíz '/').
    Evalúa el estado de autenticación y el rol del usuario para redirigirlo
    de manera automática a su panel de control correspondiente:
      - Administrador  -> Panel de Administrador (attendance:admin_dashboard)
      - Profesor       -> Panel Docente (attendance:profesor_dashboard)
      - Estudiante     -> Portal del Estudiante (attendance:estudiante_dashboard)
      - No autenticado -> Página de Información Pública (attendance:public_info)
    """
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('attendance:public_info')

        if request.user.is_admin:
            return redirect('attendance:admin_dashboard')
        elif request.user.is_profesor:
            return redirect('attendance:profesor_dashboard')
        elif request.user.is_estudiante:
            return redirect('attendance:estudiante_dashboard')
        else:
            return redirect('attendance:public_info')


class CustomLoginView(LoginView):
    """
    Vista personalizada para el inicio de sesión de usuarios.
    Utiliza el formulario estilizado LoginForm y redirige al home inteligente tras autenticar.
    """
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos.')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    """
    Vista personalizada para el cierre de sesión seguro del usuario.
    Notifica mediante mensaje informativo y redirige al formulario de login.
    """
    next_page = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Has cerrado sesión exitosamente.')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    """
    Vista de registro de nuevos usuarios en el sistema.
    - Abierta al público para registrarse como Estudiante o Profesor.
    - Si un Administrador la visita, tiene permisos para crear usuarios de cualquier rol.
    """
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_admin'] = self.request.user.is_authenticated and self.request.user.is_admin
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        rol_creado = self.object.get_role_display()
        if not self.request.user.is_authenticated:
            messages.success(
                self.request,
                f'¡Cuenta creada exitosamente como {rol_creado}! Ya puedes iniciar sesión con tu usuario "{self.object.username}".'
            )
            return redirect('accounts:login')
        else:
            messages.success(
                self.request,
                f'Usuario "{self.object.username}" ({rol_creado}) creado exitosamente.'
            )
            return redirect('attendance:admin_dashboard')


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Vista que permite a cualquier usuario autenticado actualizar su información
    de perfil, datos de contacto y fotografía personal.
    """
    model = User
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado exitosamente.')
        return super().form_valid(form)
