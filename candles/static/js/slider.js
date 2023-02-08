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
            autoplay: {
                delay: 3000,
                pauseOnMouseEnter: true
            },
            breakpoints: {
                1024: {
                    slidesPerView: 3,
                    slidesPerGroup: 3,
                },
                600: {
                    slidesPerView: 2,
                    slidesPerGroup: 2,
                },
                360: {
                    slidesPerView: 1,
                    slidesPerGroup: 1,
                },
            },
            loop: true,
            spaceBetween: 10,
            pagination: {
                el: '.gallery__swiper-pagination',
                clickable: true,
            },
        });
    };
    swiperGalleryInit();
});
