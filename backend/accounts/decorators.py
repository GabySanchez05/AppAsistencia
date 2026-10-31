from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages


def admin_required(view_func):
    """Decorador que restringe el acceso solo a Administradores."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.is_admin:
            messages.error(request, 'Solo los administradores tienen acceso a esta sección.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def profesor_required(view_func):
    """Decorador que restringe el acceso a Profesores y Administradores."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not (request.user.is_profesor or request.user.is_admin):
            messages.error(request, 'Solo los profesores y directivos pueden gestionar asistencias.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


# Alias para compatibilidad con código existente
gestor_required = profesor_required


def staff_required(view_func):
    """Decorador que permite acceso a Admin o Profesor."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not (request.user.is_admin or request.user.is_profesor):
            messages.error(request, 'No tienes permiso para acceder a esta página.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
