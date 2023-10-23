// Global constant variables
const photoFileInputLabel = document.getElementById('photo-file-input-label');
const photoFileInput = document.getElementById('photo-file-input');
const myInput = document.querySelector("#date_time");
const baseURLCommunityEvents = "https://damp-castle-86239-1b70ee448fbdevents/";
const postCommunityEventMethod = 'POST';

// Initialize flatpickr date picker
const fp = flatpickr(myInput, {
    enableTime: true,
    dateFormat: "Y-m-d H:i"
});

// FormData for POST request
const formData = new FormData();
formData.append("name", "Yoga in a tree 4");
formData.append("location", "Morningside Forest");
formData.append("organiser", "Morningside Community Wellness Collective");
formData.append("event_type", "Group Activity");
formData.append("description", "Doing yoga in a tree");
formData.append("date_time", "2023-10-21 17:30");
formData.append("photo", photoFileInput.files[0], "icons8-software-80.png");
formData.append("website_code", "Pete123");

// Function to update aria-hidden attribute for menus
const updateAriaAttributes = () => {
    const width = window.innerWidth;
    const headerMenu = document.getElementsByClassName("flex-document")[0];
    // Add your logic for updating aria-hidden here
};

// Function to handle form submission
const handleFormSubmit = event => {
    event.preventDefault();
    formData.append("website_code", my_website_code);

    const requestOptions = {
        method: postCommunityEventMethod,
        body: formData,
        redirect: 'follow'
    };

    fetch(baseURLCommunityEvents, requestOptions)
        .then(response => response.json())
        .then(data => {
            if (!response.ok) {
                console.log("Server response:", data);
                throw new Error("Network response was not ok");
            }
            console.log(data.description);
            alert('Your event "' + data.description + '" has been added to our website! Thanks!');
            eventForm.reset();
            photoFileInputLabel.textContent = "Add Photo (Optional)";
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

// Page setup on first load
fetch(baseURLCommunityEvents, requestOptions)
    .then(response => response.json())
    .then(data => {
        if (!response.ok) {
            console.log("Server response:", data);
            throw an Error("Network response was not ok");
        }
        console.log(data.description);
    })
    .catch(error => {
        console.error("There was a problem with the fetch operation:", error.message);
    });

// Function to fetch events from the API and render them
const fetchAndRenderEvents = () => {
    fetch(urlWithParams, requestOptions)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((events) => {
            // Clear the eventsContainer
            while (eventsContainer.firstChild) {
                eventsContainer.removeChild(eventsContainer.firstChild);
            }

            // Handle the events data here (e.g., display or process it)
            events.forEach((event) => {
                const eventTemplate = `
                    <article class="col-12 col-md-12 col-lg-6">
                        <div class="card" role="group" aria-labelledby="card${event.id}-title" aria-describedby="card${event.id}-desc">
                            <h2 class="card-header p-2" id="card${event.id}-title">${event.name}</h2>
                            <img class="card-banner-image" src="${event.photo}" alt="${event.name}">
                            <p class="card-body-text p-2">${event.description}</p>
                            <p class="card-body-text px-2"><strong>Location:</strong> ${event.location}</p>
                            <p class="card-body-text px-2"><strong>Organiser:</strong> ${event.organiser}</p>
                            <p class="card-body-text px-2"><strong>Event Type:</strong> ${event.event_type}</p>
                            <p class="card-body-text px-2"><strong>Date & Time:</strong> ${new Date(event.date_time)}</p>
                        </div>
                    </article>
                `;

                eventsContainer.innerHTML += eventTemplate;
            });
        })
        .catch((error) => {
            // Handle any errors that occurred during the fetch
            console.error("Error processing events:", error.message);
            alert("There was a problem loading events. Please refresh the page.");
        });
};

// Call the function to fetch and render events on page load
fetchAndRenderEvents();

// Additional functions for triggering file input and handling file change
const triggerFileInput = () => {
    // Function logic here
};

const handleFileChange = () => {
    // Function logic here
};