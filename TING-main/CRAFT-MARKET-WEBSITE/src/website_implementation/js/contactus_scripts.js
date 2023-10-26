document.addEventListener('DOMContentLoaded', function() {
       // Accessing form elements to handle user interactions with the contact form
    const contactForm = document.querySelector('.contact-form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageTextarea = document.getElementById('message');

    
     // Elements to provide feedback to the user after form interactions
    const feedbackMessage = document.getElementById('feedbackMessage');
    const formFeedback = document.getElementById('formFeedback');

    // Buttons to clear and submit the form
    const clearBtn = document.getElementById('clearBtn');
    const sendBtn = document.getElementById('sendBtn');

    // Newsletter elements
    const newsletterInput = document.querySelector('footer input[type="email"]');
    const newsletterBtn = document.querySelector('footer button');
    const newsletterFeedback = document.getElementById('newsletterFeedback');

     // Function to reset the contact form fields
    function clearContactForm() {
        nameInput.value = '';
        emailInput.value = '';
        messageTextarea.value = '';
    }

     // Function to handle the contact form submission
    function submitContactForm() {
        // Check if all required fields are filled before proceeding
        if (nameInput.value && emailInput.value && messageTextarea.value) {
            feedbackMessage.style.display = 'block';
            clearContactForm();
        } else {
            formFeedback.style.display = 'block';
        }
    }

    function submitNewsletter() {
            // Check if the email field is filled before proceeding
        if (newsletterInput.value) {
            // Provide positive feedback to the user and reset the input
            alert('Thank you for subscribing to our newsletter!');
            newsletterInput.value = '';
        } else {
            // Provide negative feedback to the user
            newsletterFeedback.style.display = 'block';
        }
    }

    // Clear form fields
    clearBtn.addEventListener('click', function(e) {
        e.preventDefault();
        clearContactForm();
    });

    // Form submission feedback
    sendBtn.addEventListener('click', function(e) {
        e.preventDefault();
        submitContactForm();
    });

    // Newsletter Signup
    newsletterBtn.addEventListener('click', function(e) {
        e.preventDefault();
        submitNewsletter();
    });
});
