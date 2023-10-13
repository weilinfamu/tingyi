$(document).ready(function() {
  let currentSlide = 0;
  const slides = $('.carousel .slide');
  const slideWidth = $(slides[0]).outerWidth();
  const numberOfSlides = slides.length;

  // Add clones to the beginning and end
  $('.carousel').prepend($(slides[slides.length - 1]).clone());
  $('.carousel').append($(slides[0]).clone());

  // Adjust the carousel width and initial position
  $('.carousel').css('width', slideWidth * (numberOfSlides + 2) + 'px');
  $('.carousel').css('transform', 'translateX(' + (-slideWidth) + 'px)');

  $('#next').click(function() {
      currentSlide++;
      if (currentSlide > numberOfSlides) {
          currentSlide = 1;
          $('.carousel').css('transition', 'none');
          $('.carousel').css('transform', 'translateX(' + (-slideWidth) + 'px)');
          setTimeout(() => {
              $('.carousel').css('transition', 'transform 0.4s ease-in-out');
              nextSlide();
          });
          return;
      }
      nextSlide();
  });

  $('#prev').click(function() {
      currentSlide--;
      if (currentSlide < 0) {
          currentSlide = numberOfSlides - 1;
          $('.carousel').css('transition', 'none');
          $('.carousel').css('transform', 'translateX(' + (-slideWidth * numberOfSlides) + 'px)');
          setTimeout(() => {
              $('.carousel').css('transition', 'transform 0.4s ease-in-out');
              prevSlide();
          });
          return;
      }
      prevSlide();
  });

  function nextSlide() {
      $('.carousel').css('transform', 'translateX(' + (-slideWidth * (currentSlide + 1)) + 'px)');
  }

  function prevSlide() {
      $('.carousel').css('transform', 'translateX(' + (-slideWidth * (currentSlide + 1)) + 'px)');
  }
});
