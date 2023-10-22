$(document).ready(function() {
    let currentSlide = 0;
    const slides = $('.carousel .slide');
    const slideWidth = $(slides[0]).outerWidth();
    const numberOfSlides = slides.length;

    // Adjust the carousel width and initial position
    $('.carousel').css('width', slideWidth * numberOfSlides + 'px');

    $('#next').click(function() {
        moveToNextSlide();
    });

    $('#prev').click(function() {
        moveToPreviousSlide();
    });

    // 添加3秒轮播效果
    setInterval(moveToNextSlide, 3000);

    function moveToNextSlide() {
        currentSlide++;
        if (currentSlide >= numberOfSlides) {
            currentSlide = 0;
        }
        updateSlide();
    }

    function moveToPreviousSlide() {
        currentSlide--;
        if (currentSlide < 0) {
            currentSlide = numberOfSlides - 1;
        }
        updateSlide();
    }

    function updateSlide() {
        $('.carousel').css('transform', 'translateX(' + (-slideWidth * currentSlide) + 'px)');
    }
});
