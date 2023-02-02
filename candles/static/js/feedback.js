//Import Function
import loadContent from './catalog';

function feedbackForm(){
    $('.feedback-form').on('submit', function(e){
        e.preventDefault();
        let form = $(this)
        let formURL = form.attr('action');
        let data = new FormData();
        let form_array = form.serializeArray();
        for (let i = 0; i < form_array.length; i++){
            data.append(form_array[i].name, form_array[i].value);
        }
        $.ajax({
            url: formURL,
            data:  data,
            processData: false,
            contentType: false,
            method: 'POST',
            success: function(data) {
                if (form.hasClass('basket__form')){
                    if (data['success']){
                        $('.basket-info-js').replaceWith(data['html']);
                        loadContent('/clear_cart/');
                    }
                    else {
                        form.replaceWith(data['html']);
                    }
                }
                else {
                    form.replaceWith(data['html']);
                }
                feedbackForm();
            },
        });

    });
}

feedbackForm();

//Export Function
export default feedbackForm;
