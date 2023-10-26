document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        // Prevent the default form submission to handle it manually
        event.preventDefault();

        // Assume all fields are filled until proven otherwise
        let allFieldsFilled = true;

        // Get all relevant input fields from the form
        const inputs = form.querySelectorAll("input[type='text'], input[type='email'], input[type='password'], input[type='tel']");
        // Check if any input field is empty
        inputs.forEach(input => {
            if (!input.value) {
                allFieldsFilled = false;
            }
        });
        /*Notify the user if not all fields are filled*/
        if (!allFieldsFilled) {
            alert("Please fill out all fields before submitting.");
            return;
        }
        // Ensure the user has verified they're not a robot
        const captchaChecked = document.querySelector("#captcha").checked;
        if (!captchaChecked) {
            alert("Please confirm that you're not a robot.");
            return;
        }

        alert("Registration successful!");
       
    });
});
