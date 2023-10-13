$(document).ready(function() {
  let currentSlide = 0;
  const slides = $('.carousel .slide');
  const slideWidth = $(slides[0]).outerWidth();
  const numberOfSlides = slides.length;

  slides.each((index, slide) => {
    $(slide).css('left', `${index * slideWidth}px`);
  });

  $('#next').click(nextSlide);

  $('#prev').click(function() {
    currentSlide = (currentSlide - 1 + numberOfSlides) % numberOfSlides;
    updateSlides();
  });

  function nextSlide() {
    console.log("Entering nextSlide function");  // New log statement
    currentSlide = (currentSlide + 1) % numberOfSlides;
    updateSlides();
    console.log("Exiting nextSlide function");   // New log statement
  }

  function updateSlides() {
    console.log("Entering updateSlides function");   // New log statement
    slides.each((index, slide) => {
      const newPosition = (index - currentSlide) * slideWidth;
      $(slide).css('left', `${newPosition}px`);
    });
    console.log("Exiting updateSlides function");    // New log statement
  }

  setInterval(nextSlide, 6000);
});
