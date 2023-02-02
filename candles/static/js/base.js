// Scroll animation
$('.scroll-js').click(function(e){
    e.preventDefault();
    let header = $('.header');
    let header_menu = header.find('.header__menu');
    let burger = $('.header__burger')
    if (header_menu.hasClass('active')){
        header_menu.removeClass('active');
    }
    if (burger.hasClass('active')){
        burger.removeClass('active');
    }
    $('html, body').stop().animate({
        scrollTop: $($(this).attr('href')).offset().top - header.height()
    }, 1000, 'swing');
});

//Init Phone Mask
$(document).on('focus', 'input[name*="phone"]', function() {
    $(this).mask('+7(999)999-99-99');
});

//Init Index Mask
$(document).on('focus', 'input[name*="index"]', function() {
    $(this).mask('999-999');
});

//Stick header on load
$(function () {
    let header = $('.header');
    scroll = $(window).scrollTop();
    if (scroll > 0) header.addClass('sticky');
});

//Stick header on scroll
//$(window).scroll(function(){
//  var header = $('.header'),
//      scroll = $(window).scrollTop();
//
//  if (scroll > 0) header.addClass('sticky');
//  else header.removeClass('sticky');
//});

//Init AOS Animation
import AOS from 'aos';

$(function() {
    AOS.init({
        offset: 200,
        once: true,
    });
});

//Mobile Menu
$(".header__burger").on("click", function(event) {
    event.preventDefault();
    $(this).toggleClass("active");
    $('.header__menu').toggleClass('active');
    $('.header__menu').addClass('anim--active');
    $("body").toggleClass("noscroll");
});
