// Hide gallery photos

function hideImages(){
    $('.gallery__grid .gallery__image-link').slice(6,).hide();
}
hideImages();

function showImages(){
    $('.gallery__grid .gallery__image-link:hidden').slice(0, 6).show()
}

$('.show-more-js').click(function(e){
    e.preventDefault();
    showImages();
});
