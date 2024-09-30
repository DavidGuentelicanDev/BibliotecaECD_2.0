$(document).ready(function() {
    $('#btn_cerrarSesion').click(function(event) {
        event.preventDefault();

        Swal.fire({
            title: 'Cerrar sesión',
            text: '¿Estás seguro de cerrar la sesión? Perderás cualquier avance que no hayas guardado',
            showCancelButton: true,
            confirmButtonText: 'Salir',
            cancelButtonText: 'Cancelar',
        }).then((result) => {
            if (result.isConfirmed) {
                $('#form_logout').submit();//si el usuario confirma se envia el formulario
                //muestra el efecto de carga antes de realizar el cierre de sesion
                Swal.fire({
                    title: 'Cerrando sesión',
                    allowOutsideClick: false,
                    didOpen: () => {
                        Swal.showLoading(); //efecto de carga
                    }
                });
            }
        });
    });
});
