// Base URL of the open Meteo API endpoint
const baseUrl = 'https://api.open-meteo.com/v1/forecast';   //const means that it can not be changed    

//Query parameters as a JavaScript object
const queryParams = {
    latitude:29.5,
    longitude:106.5,
    current_weather:true,
}

//Convert the query parameters object into a query string
const queryString = new URLSearchParams(queryParams).toString();

//Full URL with query parameters
//const urlwithParams = baseUrl + '?' + queryString;
const urlwithParams = baseUrl+"?"+queryString;

//Request options
const requestOption = {
    method: 'GET',
    redirect: 'follow'
};

//Making the fetch call
fetch(urlwithparams, requestOptions)
.then(response => response.json())
.then(data => {
    const weather = data.current_weather;
    console.log("Current temperature: " + weather.temperature + "c");

    const temperature_element = document.getElementById('current_temperature');
    const windspeed_element = document.getElementById('current_windspeed');
    temperature_element.innerText = weather.temperature + "c";
    windspeed_element.innerText = weather.windspeed + "km/h";
})
.catch(error => console.log('error', error));

const subscribeForm = document.getElementById('subscribe_form');

const handleInputChange = () => {
    let firstName = document.getElementById('firstName').value;
    let suburb = document.getElementById('suburb').value;
    let email = document.getElementById('email').value;
    let responseMessage = document.getElementById('responseMessage');

    responseMessage.textContent = "Sending your request, please wait...";
    let payload = {
    subscriber_name: firstName,
    subscriber_suburb: suburb,
    subscriber_email: email
    };


    if (firstName.value && suburb.value && email.value && email.validity.valid) {
        button.classList.add('enabled');
        button.disabled = false;
    } else {
        button.classList.remove('enabled');
        button.disabled = true;
    }
};

const handleSubmit = (event) => {
    event.preventDefault();
    // Your code for handling form submission goes here
  };
  

  // Using the Fetch API to make an HTTP request
fetch(url, {
    method: method,                   // Specify the HTTP method (e.g., 'POST')
    headers: headers,                 // Define HTTP headers (e.g., content type)
    body: JSON.stringify(payload)     // Convert payload to JSON and set it as the request body
  })
    .then((response) => response.text())  // Convert the response to text format
    .then((data) => {                     // Handle the data received from the response
      if (data === 'added') {              // Check if the response data is 'added'
        responseMessage.textContent = 'Subscription successful. Thank you for subscribing!';
      } else if (data === 'exists') {      // Check if the response data is 'exists'
        responseMessage.textContent = 'This email address has already been used to subscribe.';
      } else if (data === 'error') {       // Check if the response data is 'error'
        responseMessage.textContent = 'An error occurred with the API. Please try again later.';
      } else {
        // Handle an unexpected response from the API
        responseMessage.textContent = 'An unexpected response from the API. Please try again later.';
      }
    })
    .catch((error) => {  // Handle errors that occur during the fetch operation
      console.error('Error:', error);  // Log the error to the console
      responseMessage.textContent = 'An unexpected error occurred. Please try again later.';
    });
  



const url = 'https://damp-castle-86239-1b70ee448fbd.herokuapp.com/decoapi/api/';
const method = 'POST';
const headers = {
  'Content-Type': 'application/json' // Corrected the format
};
subscribeForm.addEventListener('submit', handleSubmit);
subscribeForm.addEventListener('input', handleInputChange);