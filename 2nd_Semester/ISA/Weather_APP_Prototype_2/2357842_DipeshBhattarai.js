// ! MY API KEY ⬇️...
const apiKey = "345752d369b66791e891af7fae98eb67";

// fetching api data from open weather map
async function getWeatherApi(city) {
  try {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
    const response = await fetch(url);
    const weatherData = await response.json();

    if (weatherData.cod === "404") {
      alertBox("Oopps!! City not found.", "rgba(120, 180, 230, 0.9)");
    } else {
      getWeather(weatherData);
    }

  } catch (error) {
    console.error("Error fetching weather data:", error);
  }
}

// get the current date
function getDate(weatherData) {
  let unixtime = weatherData;
  let date = new Date(unixtime * 1000); // Convert Unix timestamp to milliseconds

  // Extract the month, day, and year from the date object
  let month = date.getMonth() + 1; // Add 1 because months are zero-indexed
  let day = date.getDate();
  let year = date.getFullYear();



  // Create a new Date object with the extracted components
  let formattedDate = new Date(year, month - 1, day);


  const options = { weekday: "long", month: "long", day: "numeric" };
  return formattedDate.toLocaleDateString(undefined, options);
}

// stores the data from api in variables
function getWeather(weatherData) {
  const { name } = weatherData;
  const { icon, description, main } = weatherData.weather[0];
  const { temp: temperature, humidity, pressure } = weatherData.main;
  const { speed: windSpeed } = weatherData.wind;
  const { dt } = weatherData;

  const currentDate = getDate(dt);

  let realTemperature = Math.floor(temperature)

  displayWeather(
    name,
    icon,
    description,
    realTemperature,
    humidity,
    windSpeed,
    pressure,
    currentDate,
    main
  );


  // Split the string by the comma
  let dateComponent = currentDate.split(', ');

  let day_of_week = dateComponent[0];
  let date = dateComponent[1];
  let dataWeather = {
    temperature,
    description: main,
    city: name,
    day_of_week,
    date,
    icon
  }

  fetch('2357842_DipeshBhattarai_weatherhistory.php', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(dataWeather),
  })
    .then(response => response.text())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error:', error);
    });

}

// displays the data from api in frontend
function displayWeather(
  name,
  icon,
  description,
  temperature,
  humidity,
  windSpeed,
  pressure,
  currentDate
) {

  fetch('2357842_DipeshBhattarai_getweatherdata.php')
    .then(response => response.json())
    .then(data => {
      const weatherHistoryDiv = document.getElementById('weatherHistory');

      const weatherCardsHTML = data.map(entry => `
      <div class="weather-card">
        <div>${entry.date}</div>
        <div>${entry.day_of_week}</div>
        <img src="https://openweathermap.org/img/wn/${entry.icon}.png" alt="${entry.description}">
        <div>${entry.temperature}°C</div>
        <div>${entry.description}</div>
      </div>
    `).join('');

      weatherHistoryDiv.innerHTML = weatherCardsHTML;
    })
    .catch(error => console.error('Error fetching weather data:', error));


  document.querySelector(".city").innerText = name;
  document.querySelector(".temp").innerText = temperature + "°C";
  document.querySelector(".description").innerText =
    description.charAt(0).toUpperCase() + description.slice(1);
  document.querySelector(
    ".icon"
  ).src = `https://openweathermap.org/img/wn/${icon}.png`;
  document.querySelector(".humidity").innerText = `Humidity: ${humidity}%`;
  document.querySelector(".wind").innerText = `Wind: ${windSpeed}km/hr`;
  document.querySelector(".pressure").innerText = `Pressure: ${pressure} Pa`;
  document.querySelector(".date").innerText = currentDate;
}

// passes the search input in getWeatherApi function
function search() {
  getWeatherApi(document.querySelector(".search-input").value);
}

// displays if the user inputs the invalid city name
function alertBox(message, color) {
  const alertBox = document.createElement("div");
  alertBox.textContent = message;
  alertBox.classList.add("alert");
  alertBox.style.backgroundColor = color;
  document.body.insertBefore(alertBox, document.body.firstChild);

  setTimeout(function () {
    alertBox.remove();
  }, 1500);
}

// executes only when html document is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("buttonClick").addEventListener("click", function () {
    search();
  });

  // when pressing enter key search function is called
  document
    .querySelector(".search-input")
    .addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        search();
      }
    });

  // This is my default location
  getWeatherApi("Cullman");
});


