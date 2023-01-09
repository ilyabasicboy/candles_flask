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
});
