"""
Configuración general de Django para el proyecto AppAsistencia.
Subproyecto: Desarrollo de Aplicaciones 1.
"""

import os
from pathlib import Path

# Directorio raíz del proyecto (backend/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para entornos de desarrollo (se sobreescribe con variables de entorno en producción)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-change-me-in-production')

# Modo de depuración (activado en desarrollo para recarga automática de archivos)
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('true', '1', 'yes')

# Hosts permitidos para recibir peticiones HTTP
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# --------------------------------------------------------------------------
# Definición de Aplicaciones Instaladas
# --------------------------------------------------------------------------

INSTALLED_APPS = [
    # Aplicaciones estándar de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Librerías externas / terceros
    'rest_framework',
    'corsheaders',

    # Aplicaciones locales del proyecto
    'accounts',    # Gestión de usuarios, roles y autenticación
    'attendance',  # Gestión de grados, estudiantes y asistencias
    'core',        # Mixins de seguridad y comandos de inicialización
]

# --------------------------------------------------------------------------
# Middleware del Sistema
# --------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo principal de enrutamiento URL
ROOT_URLCONF = 'config.urls'

# --------------------------------------------------------------------------
# Configuración del Motor de Plantillas (Templates)
# --------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Procesador de contexto personalizado para inyectar roles en el navbar
                'accounts.context_processors.user_role',
            ],
        },
    },
]

# Configuración de la aplicación WSGI para el servidor web
WSGI_APPLICATION = 'config.wsgi.application'

# --------------------------------------------------------------------------
# Base de Datos (PostgreSQL 16)
# --------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'app_asistencia'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# --------------------------------------------------------------------------
# Modelo de Usuario Personalizado con Roles
# --------------------------------------------------------------------------

AUTH_USER_MODEL = 'accounts.User'

# --------------------------------------------------------------------------
# Validadores de Contraseña
# --------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------------------------
# Internacionalización y Localización
# --------------------------------------------------------------------------

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_TZ = True

# --------------------------------------------------------------------------
# Archivos Estáticos (CSS, JavaScript, Fuentes)
# --------------------------------------------------------------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --------------------------------------------------------------------------
# Archivos Multimedia (Imágenes de perfil subidas por usuarios)
# --------------------------------------------------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------------------------------
# URLs de Autenticación y Redirección de Sesión
# --------------------------------------------------------------------------

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# --------------------------------------------------------------------------
# Configuración de CORS (Cross-Origin Resource Sharing)
# --------------------------------------------------------------------------

CORS_ALLOWED_ORIGINS = os.environ.get(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000'
).split(',')

CORS_ALLOW_CREDENTIALS = True

# --------------------------------------------------------------------------
# Django REST Framework
# --------------------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# --------------------------------------------------------------------------
# Tipo de campo de clave primaria por defecto
# --------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
