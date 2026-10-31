"""
Configuración principal de rutas URL para el proyecto AppAsistencia.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import HomeView

urlpatterns = [
    # Panel de administración de Django (Django Admin)
    path('admin/', admin.site.urls),

    # Módulo de autenticación, usuarios y perfiles
    path('accounts/', include('accounts.urls')),

    # Página de inicio con redirección inteligente según rol del usuario
    path('', HomeView.as_view(), name='home'),

    # Módulo principal de asistencia escolar y vistas por roles
    path('', include('attendance.urls')),
]

# Servir archivos multimedia (imágenes de perfil) en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
