//Import swiper
import Swiper, {
    Navigation,
    Pagination,
    EffectFade,
    Autoplay,
    Thumbs
} from 'swiper';

Swiper.use([
    Navigation,
    Pagination,
    EffectFade,
    Autoplay,
    Thumbs
]);

$(function () {

    //Init Intro Slider
    function swiperCatalogInit() {
        const swiper = new Swiper('.swiper', {
          speed: 300,
          spaceBetween: 100,
          loop: true,
          autoplay: {
              delay: 3000,
              pauseOnMouseEnter: true,
          },
          pagination: {
              el: '.swiper-pagination',
              type: 'bullets',
              clickable: true,
          },
          navigation: {
              nextEl: ".swiper-button-next",
              prevEl: ".swiper-button-prev",
          },
        });
    };
    swiperCatalogInit();
});
