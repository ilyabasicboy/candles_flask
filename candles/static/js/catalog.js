// Catalog Basket
function uploadBasketInfo(){
    $('.catalog-btn-ajax').on('click', function(e){
        e.preventDefault();
        let product_id = $(this).data('product');
        //Load Content
        $.get($(this).attr('href'), function(data){

            // Change products info in catalog
            if (data['clear_cart']){
                $('.product-info-js').html(data['catalog_btn_template']);
                $('.product-info-js').map(function(index, element){
                    let product_id = $(element).data('product');
                    let url = $(element).data('href');
                    $(element).find('.catalog-btn-ajax').data('product', product_id).attr('href', url);
                });
            }
            else {
                $(`.product-info-js[data-product=${product_id}]`).html(data['catalog_btn_template']);
            }
            $('.basket-info-js').html(data['basket_info']);
           uploadBasketInfo();
        });
    });
}

uploadBasketInfo();
