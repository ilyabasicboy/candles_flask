$(function () {
    //Form Modal
    function initDefaultModal() {
        $('.modal-open').each(function() {
            $(this).magnificPopup({
                type: "inline",
                removalDelay: 500,
                mainClass: 'mfp-move',
                callbacks: {
                    open: function () {
                        $("body").addClass("noscroll");
                    },
                    close: function () {
                        $("body").removeClass("noscroll");
                    },
                },
            });
        });
    }
    initDefaultModal();

    //Close Modal With Scroll
    $(document).on('click', '.close-modal', function(){
        $.magnificPopup.close();
    });


    //Gallery Modal
    $('.mfp-gallery').each(function() {
        $(this).magnificPopup({
            type: 'image',
            removalDelay: 500,
            mainClass: 'mfp-fade',
            image: {
                cursor: null,
                tClose: 'Закрыть',
                titleSrc: function(item) {
                    return item.img.attr('alt');
                }
            },
            gallery: {
                enabled: true,
                preload: [0, 2],
                navigateByImgClick: true,
                tPrev: 'Предыдущее фото',
                tNext: 'Следующее фото'
            },
            delegate: 'a[href][target!="_blank"]',
            callbacks: {
                buildControls: function() {
                    if (this.items.length > 1) {
                        this.contentContainer.append(this.arrowLeft.add(this.arrowRight));
                    }
                },
                open: function() {
                    $("body").addClass("noscroll");
                },
                close: function() {
                    $("body").removeClass("noscroll");
                }
            },
            closeMarkup: '<button title="Закрыть" type="button" class="mfp-close"></button>',
        });
    });
});
