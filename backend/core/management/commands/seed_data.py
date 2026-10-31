"""
Comando personalizado de Django para aprovisionar los usuarios iniciales del sistema.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Crea únicamente los usuarios base del sistema (Admin, Profesor, Estudiante) sin registros de datos escolares.'

    def handle(self, *args, **options):
        self.stdout.write('Verificando usuarios iniciales...')

        # 1. Administrador (Superusuario con acceso completo a Django Admin)
        admin_user, _ = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@colegio.edu',
                'first_name': 'Director',
                'last_name': 'General',
                'role': User.Role.ADMIN,
                'is_staff': True,
                'is_superuser': True,
            }
        )
        admin_user.set_password('Admin123!')
        admin_user.role = User.Role.ADMIN
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        # 2. Profesor
        profesor_user, _ = User.objects.get_or_create(
            username='profesor',
            defaults={
                'email': 'profesor@colegio.edu',
                'first_name': 'Carlos',
                'last_name': 'Mendoza',
                'role': User.Role.PROFESOR,
                'is_staff': False,
            }
        )
        profesor_user.set_password('Profesor123!')
        profesor_user.role = User.Role.PROFESOR
        profesor_user.save()

        # 3. Estudiante
        estudiante_user, _ = User.objects.get_or_create(
            username='estudiante',
            defaults={
                'email': 'estudiante@colegio.edu',
                'first_name': 'Mateo',
                'last_name': 'Pérez',
                'role': User.Role.ESTUDIANTE,
                'is_staff': False,
            }
        )
        estudiante_user.set_password('Estudiante123!')
        estudiante_user.role = User.Role.ESTUDIANTE
        estudiante_user.save()

        # Limpiar cualquier usuario gestor obsoleto
        User.objects.filter(username='gestor').delete()

        self.stdout.write(self.style.SUCCESS('Usuarios base listos:'))
        self.stdout.write('  - admin / Admin123!')
        self.stdout.write('  - profesor / Profesor123!')
        self.stdout.write('  - estudiante / Estudiante123!')
