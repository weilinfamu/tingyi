document.addEventListener('DOMContentLoaded', function() {
    // Form elements
    const contactForm = document.querySelector('.contact-form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageTextarea = document.getElementById('message');
    const feedbackMessage = document.getElementById('feedbackMessage');
    const formFeedback = document.getElementById('formFeedback');
    const clearBtn = document.getElementById('clearBtn');
    const sendBtn = document.getElementById('sendBtn');

    // Newsletter elements
    const newsletterInput = document.querySelector('footer input[type="email"]');
    const newsletterBtn = document.querySelector('footer button');
    const newsletterFeedback = document.getElementById('newsletterFeedback');

    function clearContactForm() {
        nameInput.value = '';
        emailInput.value = '';
        messageTextarea.value = '';
    }

    function submitContactForm() {
        if (nameInput.value && emailInput.value && messageTextarea.value) {
            feedbackMessage.style.display = 'block';
            clearContactForm();
        } else {
            formFeedback.style.display = 'block';
        }
    }

    function submitNewsletter() {
        if (newsletterInput.value) {
            alert('Thank you for subscribing to our newsletter!');
            newsletterInput.value = '';
        } else {
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
