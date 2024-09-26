$(document).ready(function() {
    $('#btn_loginAdmin').click(function(event) {
        event.preventDefault(); //previene el comportamiento predeterminado del boton (submit en este caso)

        let correo = $('#txt_correoAdmin').val().trim();
        let contrasena = $('#txt_contrasenaAdmin').val().trim();
        let url = '/app_admin/login_admin/';

        if (correo == '' || contrasena == '') {
            Swal.fire({
                title: 'Campos obligatorios',
                text: 'Debes indicar un usuario y una clave válidos para iniciar sesión',
                icon: 'warning',
                confirmButtonText: 'OK'
            });

            return;
        }

        //ajax para capturar los jsonresponse
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                correoAdmin: correo,
                contrasenaAdmin: contrasena,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function(response) {
                console.log(response); //para ver que respuesta obtengo
                if (response.success) {
                    Swal.fire({
                        title: 'Credenciales válidas',
                        text: 'Redirigiendo a la página principal...',
                        icon: 'success',
                        timer: 1000,
                        showConfirmButton: false,
                        didOpen: () => {
                            Swal.showLoading();
                        },
                        willClose: () => {
                            window.location.href = '/app_admin/home/';
                        }
                    });
                } else {
                    Swal.fire({
                        title: 'Error',
                        text: response.message,
                        icon: 'error',
                        confirmButtonText: 'OK'
                    });
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr); //para ver que dice el error
                console.log(errmsg); //para ver que dice el error
                console.log(err); //para ver que dice el error
                Swal.fire({
                    title: 'Error',
                    text: 'Hubo un error al intentar iniciar sesión. Por favor, intenta nuevamente más tarde.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        });
    });
});
