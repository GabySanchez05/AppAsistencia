/**
 * AppAsistencia — Archivo JavaScript Principal
 * Manejo interactivo de interfaz de usuario, alertas y visibilidad de campos.
 */

document.addEventListener('DOMContentLoaded', function () {

    // -------------------------------------------------------------------------
    // Cierre automático de mensajes de alerta tras 5 segundos
    // -------------------------------------------------------------------------
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(function () {
                alert.remove();
            }, 500);
        }, 5000);
    });

    // -------------------------------------------------------------------------
    // Despliegue del menú de navegación en dispositivos móviles
    // -------------------------------------------------------------------------
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function () {
            navLinks.classList.toggle('active');
        });
    }

    // -------------------------------------------------------------------------
    // Visor interactivo de contraseñas (Botón con ícono de ojo)
    // Estado inicial: contraseña OCULTA -> se muestra ojo con línea diagonal
    // Al hacer clic para MOSTRAR -> aparece ojo abierto sin línea
    // Al hacer clic para OCULTAR -> aparece ojo con línea diagonal
    // -------------------------------------------------------------------------
    const toggleButtons = document.querySelectorAll('.password-toggle-btn');
    toggleButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const wrapper = this.closest('.password-wrapper');
            if (!wrapper) return;

            const input = wrapper.querySelector('input');
            const eyeOpen = this.querySelector('.eye-open-icon');
            const eyeClosed = this.querySelector('.eye-closed-icon');

            if (!input) return;

            if (input.type === 'password') {
                // Campo oculto -> hacer visible: mostrar ojo abierto, ocultar ojo con diagonal
                input.type = 'text';
                if (eyeOpen) eyeOpen.style.display = 'block';
                if (eyeClosed) eyeClosed.style.display = 'none';
                this.setAttribute('title', 'Ocultar contraseña');
                this.setAttribute('aria-label', 'Ocultar contraseña');
            } else {
                // Campo visible -> ocultar: mostrar ojo con diagonal, ocultar ojo abierto
                input.type = 'password';
                if (eyeOpen) eyeOpen.style.display = 'none';
                if (eyeClosed) eyeClosed.style.display = 'block';
                this.setAttribute('title', 'Mostrar contraseña');
                this.setAttribute('aria-label', 'Mostrar contraseña');
            }

            // Mantener el cursor activo dentro del campo de texto
            input.focus();
        });
    });

    // -------------------------------------------------------------------------
    // Resaltado visual de filas seleccionadas en tablas de asistencia
    // -------------------------------------------------------------------------
    const radioButtons = document.querySelectorAll('.attendance-table input[type="radio"]');
    radioButtons.forEach(function (radio) {
        radio.addEventListener('change', function () {
            const row = this.closest('tr');
            if (row) {
                row.querySelectorAll('.radio-cell').forEach(function (cell) {
                    cell.style.backgroundColor = '';
                });
            }
        });
    });

});
