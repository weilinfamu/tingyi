document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        let allFieldsFilled = true;
        const inputs = form.querySelectorAll("input[type='text'], input[type='email'], input[type='password'], input[type='tel']");

        inputs.forEach(input => {
            if (!input.value) {
                allFieldsFilled = false;
            }
        });

        if (!allFieldsFilled) {
            alert("Please fill out all fields before submitting.");
            return;
        }

        const captchaChecked = document.querySelector("#captcha").checked;
        if (!captchaChecked) {
            alert("Please confirm that you're not a robot.");
            return;
        }

        alert("Registration successful!");
        // Here, you can also add a logic to send the form data to the server, if needed.
    });
});
