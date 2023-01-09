//Import swiper
import Swiper, {
    Navigation,
    Pagination,
    EffectFade,
    Autoplay,
    Thumbs,
    Grid
} from 'swiper';

Swiper.use([
    Navigation,
    Pagination,
    EffectFade,
    Autoplay,
    Thumbs,
    Grid
]);

$(function () {

    //Init Catalog Slider
    function swiperCatalogInit() {
        const swiper = new Swiper('.catalog__slider', {
          speed: 300,
          spaceBetween: 100,
          loop: true,
          autoplay: {
              delay: 3000,
              pauseOnMouseEnter: true
          },
          pagination: {
              el: '.catalog__swiper-pagination',
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


    //Init Gallery Slider
    function swiperGalleryInit() {
        const swiper = new Swiper('.gallery__swiper', {
            slidesPerView: 4,
            grid: {
                rows: 2,
                fill: 'row'
            },
            autoplay: {
                delay: 3000,
            },
            spaceBetween: 10,
            pagination: {
                el: '.gallery__swiper-pagination',
                clickable: true,
            },
        });
    };
    swiperGalleryInit();
});
