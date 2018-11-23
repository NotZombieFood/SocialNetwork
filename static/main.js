function message(success_message) {
    iziToast.success({
        id: 'success',
        title: 'Success',
        message: success_message,
        position: 'bottomRight',
        transitionIn: 'bounceInLeft'
    });
}

function error(error_message) {
    iziToast.error({
        id: 'error',
        title: 'Error',
        message: error_message,
        position: 'topRight',
        transitionIn: 'fadeInDown',
        icon: 'fas fa-exclamation-triangle'
    });
}