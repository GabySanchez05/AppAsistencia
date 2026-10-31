"""
Mixins de autorización para vistas basadas en clases (CBVs) de Django.
Restringen el acceso a las vistas según el rol institucional del usuario.
"""

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin de seguridad que restringe el acceso exclusivamente a Administradores.
    Requiere que el usuario esté autenticado y que posea `is_admin=True`.
    """

    def test_func(self):
        return self.request.user.is_admin


class ProfesorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin de seguridad que permite el acceso a Profesores y Administradores.
    """

    def test_func(self):
        return self.request.user.is_profesor or self.request.user.is_admin


# Alias para mantener compatibilidad con código existente
GestorRequiredMixin = ProfesorRequiredMixin


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin de seguridad para personal institucional (Administradores o Profesores).
    """

    def test_func(self):
        return self.request.user.is_admin or self.request.user.is_profesor
