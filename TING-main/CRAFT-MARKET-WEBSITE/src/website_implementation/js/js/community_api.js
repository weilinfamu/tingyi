// Global constant variables
const photoFileInputLabel = document.getElementById('photo-file-input-label');
const photoFileInput = document.getElementById('photo-file-input');
const myInput = document.querySelector("#date_time");
const fp = flatpickr(myInput, {
    enableTime: true,
    dateFormat: "Y-m-d H:i"
});
const baseURLCommunityEvents =  "https://damp-castle-86239-1b70ee448fbd.herokuapp.com/decoapi/community_events/";
const postCommunityEventMethod = 'POST';



// Function to update aria-hidden attribute for menus

const handleFormSubmit = (event) => {
    event.preventDefault();

    // Get the form data from the event object
    let FormData = new FormData(event.target);
    formData.append("website_code", my_website_code); // Corrected the typo here

    const requestOptions = {
        method: postCommunityEventMethod,
        body: formData,
        redirect: 'follow'
    };
    
    fetch(baseURLCommunityEvents, requestOptions)
    .then(response => 
            response.json().then(data => {
            if(!response.ok) {
                console.log("server response:" , data);
                throw new Error("Network response was not ok");
            }
        return data;
            }))
        .then(data => {
            console.log(data.description);
            alert('Your event "${data.description}" has been added to our website! Thanks!');
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error.message);
            alert("Error submitting event. Please try again.");
        });
};




// Event listeners
photoFileInputLabel.addEventListener('click', triggerFileInput);
photoFileInput.addEventListener('change', handleFileChange);
eventForm.addEventListener("submit", handleFormSubmit);

