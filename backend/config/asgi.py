"""
Configuración ASGI para el proyecto AppAsistencia.
Expone la variable de nivel de módulo llamada 'application' para servidores web asíncronos ASGI.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
