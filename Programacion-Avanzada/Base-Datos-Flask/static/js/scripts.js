// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const usuarios = document.querySelectorAll('.usuario');

    usuarios.forEach(function(usuario) {
        usuario.addEventListener('click', function() {
            const nombre = this.getAttribute('data-nombre');
            const email = this.getAttribute('data-email');
            alert(`Usuario: ${nombre}\nEmail: ${email}`);
        });
    });
});
