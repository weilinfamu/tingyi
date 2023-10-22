


eventForm.addEventListener('submit', function(event) {
    console.log('Form Submitted');  // Log a message when the form is submitted
    event.preventDefault();

    const formData = new FormData(eventForm);
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
                getPostedEvents(); // Refresh the events list after a successful post
            } else {
                alert('Error posting event: ' + JSON.stringify(data));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error posting the event. Please try again.');
        });
});
flatpickr("#date_time", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",
});
// 定义常量
const baseURL = "https://damp-castle-86239-1b70ee448fbd.herokuapp.com/decoapi/community_events/";
const my_website_code = 'Pete123';
const queryParams = {
    website_code: my_website_code,
};
const queryString = new URLSearchParams(queryParams).toString();
const urlWithParams = baseURL + "?" + queryString;

const requestOptionsGET = {
    method: 'GET',
    redirect: 'follow'
};

// 使用GET请求获取之前POST的事件
function getPostedEvents() {
    fetch(urlWithParams, requestOptionsGET)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(events => {
            console.log(events);

            // 清空事件容器
            while (eventsContainer.firstChild) {
                eventsContainer.removeChild(eventsContainer.firstChild);
            }

            // 遍历每个事件并显示在页面上
            events.forEach(event => {
                const eventTemplate = `
                    <article class="col-12 col-md-12 col-lg-6">
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
        })
        .catch(error => {
            console.error("Error processing events:", error.message);
            alert("There was a problem loading events. Please refresh the page to try again.");
        });
}

// 页面首次加载时获取事件
getPostedEvents();