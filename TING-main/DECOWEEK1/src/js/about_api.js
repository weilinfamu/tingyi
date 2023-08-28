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

