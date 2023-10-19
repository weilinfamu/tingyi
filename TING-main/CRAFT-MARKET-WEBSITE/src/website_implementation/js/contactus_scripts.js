document.addEventListener('DOMContentLoaded', function() {
    // Form elements
    const contactForm = document.querySelector('.contact-form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageTextarea = document.getElementById('message');
    const feedbackMessage = document.getElementById('feedbackMessage');
    const clearBtn = document.getElementById('clearBtn');
    const sendBtn = document.getElementById('sendBtn');

    // Clear form fields
    clearBtn.addEventListener('click', function(e) {
        e.preventDefault();
        nameInput.value = '';
        emailInput.value = '';
        messageTextarea.value = '';
    });

    // Form submission feedback
    sendBtn.addEventListener('click', function(e) {
        e.preventDefault();
        if (nameInput.value && emailInput.value && messageTextarea.value) {
            feedbackMessage.style.display = 'block';
            nameInput.value = '';
            emailInput.value = '';
            messageTextarea.value = '';
        } else {
            alert('Please fill out all fields before submitting.');
        }
    });

    // Newsletter Signup
    const newsletterInput = document.querySelector('footer input[type="email"]');
    const newsletterBtn = document.querySelector('footer button');

    newsletterBtn.addEventListener('click', function(e) {
        e.preventDefault();
        if (newsletterInput.value) {
            alert('Thank you for subscribing to our newsletter!');
            newsletterInput.value = '';
        } else {
            alert('Please enter a valid email address.');
        }
    });
});
