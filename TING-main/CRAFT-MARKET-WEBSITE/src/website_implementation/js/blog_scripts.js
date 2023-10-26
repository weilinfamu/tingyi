
/*I acknowledge the use of ChatGPT (https://chat.openai.com/) to
 ensure the completion of this task. The prompts used and the response
  from ChatGPT are included in Appendix xx.
  The output from these prompts was [make sure you complete this]. 
  This usage is documented as [make sure you complete this].
  */
$(document).ready(function() {
    // Define the current slide index
    let currentSlide = 0;
     // Get all the slides in the carousel
    const slides = $('.carousel .slide');
    const slideWidth = $(slides[0]).outerWidth();

     // Calculate the total number of slides
    const numberOfSlides = slides.length;

    // Adjust the carousel width and initial position
     // This ensures that the carousel container is wide enough to hold all slides side by side
    $('.carousel').css('width', slideWidth * numberOfSlides + 'px');

     // Attach event listener to the "next" button to move to the next slide
    $('#next').click(function() {
        moveToNextSlide();
    });
    // Attach event listener to the "previous" button to move to the previous slide
    $('#prev').click(function() {
        moveToPreviousSlide();
    });

    // This creates an auto-sliding effect for the carousel 
    setInterval(moveToNextSlide, 3000);

    // Define the function to move to the next slide
    function moveToNextSlide() {
        currentSlide++;

        // Define the function to move to the next slide
        if (currentSlide >= numberOfSlides) {
            currentSlide = 0;
        }
        updateSlide();
    }

    function moveToPreviousSlide() {
        currentSlide--;
             // If we're at the beginning of the slides, loop back to the last slide
        if (currentSlide < 0) {
            currentSlide = numberOfSlides - 1;
        }
        updateSlide();
    }
        // This function translates the carousel container to the appropriate position based on the current slide index
    function updateSlide() {
        $('.carousel').css('transform', 'translateX(' + (-slideWidth * currentSlide) + 'px)');
    }
});
