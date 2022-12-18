// Scroll animation
$('.scroll-js').click(function(e){
    e.preventDefault;
    $('html, body').stop().animate({
        scrollTop: $($(this).attr('href')).offset().top
    }, 1000, 'swing');
})

//Init AOS Animation
import AOS from 'aos';

$(function() {
    AOS.init({
        offset: 200,
        once: true,
    });
});
