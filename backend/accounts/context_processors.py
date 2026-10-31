def user_role(request):
    """
    Context processor que inyecta la información del rol a todas las plantillas.
    Roles admitidos:
      - Admin: user_is_admin
      - Profesor: user_is_profesor (y alias user_is_gestor)
      - Estudiante: user_is_estudiante (y alias user_is_usuario)
    """
    if request.user.is_authenticated:
        return {
            'user_role': request.user.role,
            'user_is_admin': request.user.is_admin,
            'user_is_profesor': request.user.is_profesor,
            'user_is_gestor': request.user.is_profesor,
            'user_is_estudiante': request.user.is_estudiante,
            'user_is_usuario': request.user.is_estudiante,
            'user_role_display': request.user.get_role_display(),
        }
    return {
        'user_role': None,
        'user_is_admin': False,
        'user_is_profesor': False,
        'user_is_gestor': False,
        'user_is_estudiante': False,
        'user_is_usuario': False,
        'user_role_display': '',
    }
