document.addEventListener("DOMContentLoaded", function() {
    // Access the form element to handle event submissions
    const eventForm = document.getElementById('eventForm');
   // Access the button that toggles the visibility of the event form
    const toggleFormButton = document.getElementById('toggleFormButton');
      // Only add the click event listener if both the button and form are present in the DOM
    if (toggleFormButton && eventForm) {
        toggleFormButton.addEventListener('click', function() {
            eventForm.classList.toggle('visible');
        });
    }

        // Container where the fetched events will be displayed
    const eventsContainer = document.getElementById('eventsContainer');

    if (eventForm) {
        eventForm.addEventListener('submit', function(event) {
            console.log('Form Submitted');
            event.preventDefault();

            const formData = new FormData(eventForm);
            formData.set('website_code', my_website_code);  
            formData.set('organiser', eventForm.organizer.value);

            
            // Collect form data to send to the server
            const requestOptionsPOST = {
                method: 'POST',
                body: formData,
                redirect: 'follow'
            };
            // Send the form data to the server and handle the response
            fetch(baseURL, requestOptionsPOST)
                .then(response => response.json())
                .then(data => {
                    if (data.id) {
                         // Notify the user of successful event posting
                        alert('Event successfully posted!');
                        getPostedEvents();
                    } else {
                        // Handle any errors returned from the server
                        alert('Error posting event: ' + JSON.stringify(data));
                    }
                })
                .catch(error => {
                    // Handle any network or other errors during the fetch
                    console.error('Error:', error);
                    alert('There was an error posting the event. Please try again.');
                });
        });
    }
     // Initialize the date-time picker for better user experience
    flatpickr("#date_time", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
    });

     // Base URL for the API and website-specific code for filtering events
    const baseURL = "https://damp-castle-86239-1b70ee448fbd.herokuapp.com/decoapi/community_events/";
    const my_website_code = 'RickysWebsite';
    const queryParams = {
        website_code: my_website_code,
    };
    const queryString = new URLSearchParams(queryParams).toString();
    const urlWithParams = baseURL + "?" + queryString;

     // Define the request options for the GET request
    const requestOptionsGET = {
        method: 'GET',
        redirect: 'follow'
    };

     // Fetch and display events posted for this website
    function getPostedEvents() {
        fetch(urlWithParams, requestOptionsGET)
            .then(response => {
                
                if (!response.ok) {
                    // Handle non-200 responses
                    throw new Error(`Network response was not ok. Status: ${response.status} ${response.statusText}`);
                }
                return response.json();
            })
            .then(events => {
                console.log('Received events:', events);
                
                 // Process and display the fetched events
                if (!events || !events.length) {
                    alert("No events found.");
                    return;
                }
                function displayEventDetails(event) {
                    const latestActivity = document.getElementById('latestActivity');
                    latestActivity.innerHTML = `
                        <h2>${event.name}</h2>
                        <img src="${event.photo}" alt="${event.name}">
                        <p>${event.description}</p>
                        <p><strong>Location:</strong> ${event.location}</p>
                        <p><strong>Organiser:</strong> ${event.organiser}</p>
                        <p><strong>Event Type:</strong> ${event.event_type}</p>
                        <p><strong>Date & Time:</strong> ${new Date(event.date_time).toLocaleString()}</p>
                    `;
                }
                  // Clear the events container and populate it with the fetched events
                if (eventsContainer) {
                    while (eventsContainer.firstChild) {
                        eventsContainer.removeChild(eventsContainer.firstChild);
                    }

                    events.forEach(event => {
                        const eventTemplate = `
                            <article class="col-12 col-md-6 col-lg-4">
                                <div class="card" role="group" aria-labelledby="cards${event.id}-title" aria-describedby="cards${event.id}-desc">
                                    <h2 class="card-header p-2" id="cards${event.id}-title">${event.name}</h2>
                                    <img class="card-banner-image" src="${event.photo}" alt="${event.name}">
                                    <p class="card-body-text p-2">${event.description}</p>
                                    <p class="card-body-text px-2"><strong>Location:</strong> ${event.location}</p>
                                    <p class="card-body-text px-2"><strong>Organiser:</strong> ${event.organiser}</p>
                                    <p class="card-body-text px-2"><strong>Event Type:</strong> ${event.event_type}</p>
                                    <p class="card-body-text px-2"><strong>Date & Time:</strong> ${new Date(event.date_time).toLocaleString()}</p>
                                </div>
                            </article>
                        `;
                    
                        eventsContainer.innerHTML += eventTemplate;
                    });
                }
            })
                
            .catch(error => {
                 // Handle any errors during the fetch or processing of events
            console.error("Error processing events:", error);
            alert(`There was a problem loading events: ${error.message}. Please refresh the page to try again.`);
        });
}
    // Fetch and display events posted for this website
    getPostedEvents();
});
