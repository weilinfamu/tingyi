document.addEventListener("DOMContentLoaded", function() {
    // Ensure elements exist before accessing them
    const eventForm = document.getElementById('eventForm');
    /**
   
     * Gets the toggle form button element by its ID.
     * @type {HTMLElement}
     */
    const toggleFormButton = document.getElementById('toggleFormButton');

    if (toggleFormButton && eventForm) {
        toggleFormButton.addEventListener('click', function() {
            eventForm.classList.toggle('visible');
        });
    }
    const eventsContainer = document.getElementById('eventsContainer');

    if (eventForm) {
        eventForm.addEventListener('submit', function(event) {
            console.log('Form Submitted');
            event.preventDefault();

            const formData = new FormData(eventForm);
            formData.set('website_code', my_website_code);  
            formData.set('organiser', eventForm.organizer.value);
            const requestOptionsPOST = {
                method: 'POST',
                body: formData,
                redirect: 'follow'
            };

            fetch(baseURL, requestOptionsPOST)
                .then(response => response.json())
                .then(data => {
                    if (data.id) {
                        alert('Event successfully posted!');
                        getPostedEvents();
                    } else {
                        alert('Error posting event: ' + JSON.stringify(data));
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('There was an error posting the event. Please try again.');
                });
        });
    }

    flatpickr("#date_time", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
    });

    const baseURL = "https://damp-castle-86239-1b70ee448fbd.herokuapp.com/decoapi/community_events/";
    const my_website_code = 'RickysWebsite';
    const queryParams = {
        website_code: my_website_code,
    };
    const queryString = new URLSearchParams(queryParams).toString();
    const urlWithParams = baseURL + "?" + queryString;

    const requestOptionsGET = {
        method: 'GET',
        redirect: 'follow'
    };

    function getPostedEvents() {
        fetch(urlWithParams, requestOptionsGET)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Network response was not ok. Status: ${response.status} ${response.statusText}`);
                }
                return response.json();
            })
            .then(events => {
                console.log('Received events:', events);
    
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
            console.error("Error processing events:", error);
            alert(`There was a problem loading events: ${error.message}. Please refresh the page to try again.`);
        });
}

    getPostedEvents();
});
