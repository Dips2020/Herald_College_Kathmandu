// ! MY API KEY ⬇️...
const apiKey = "89769ff1c34f8d9fbabf6fc04056ffe8";

// Load initial city list from local storage and display the first city's weather data
document.addEventListener("DOMContentLoaded", function () {
  const cities = loadCitiesFromLocalStorage();
  if (cities.length > 0) {
    displayCitiesList(cities);
    fetchWeatherApi(cities[0]);
  }

  // Attach event listeners for search and button click
  document.getElementById("buttonClick").addEventListener("click", function () {
    const city = document.querySelector(".search-input").value;
    searchCity(city);
  });

  document.querySelector(".search-input").addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
      const city = document.querySelector(".search-input").value;
      searchCity(city);
    }
  });
});

// Function to load cities from local storage
function loadCitiesFromLocalStorage() {
  const citiesJSON = localStorage.getItem("cities");
  if (citiesJSON) {
    return JSON.parse(citiesJSON);
  } else {
    return [];
  }
}

// Function to save cities to local storage
function saveCitiesToLocalStorage(cities) {
  localStorage.setItem("cities", JSON.stringify(cities));
}

// Function to display the list of cities
function displayCitiesList(cities) {
  const citiesList = document.getElementById("citiesList");
  citiesList.innerHTML = cities.map(city => `<li>${city}</li>`).join("");

  // Attach click event to each city
  citiesList.querySelectorAll("li").forEach(cityItem => {
    cityItem.addEventListener("click", function () {
      fetchWeatherApi(cityItem.textContent);
    });
  });
}

// Function to search for a city and display its weather data
function searchCity(city) {
  const cities = loadCitiesFromLocalStorage();

  if (!cities.includes(city)) {
    cities.unshift(city);
    saveCitiesToLocalStorage(cities);
    displayCitiesList(cities);
  }
  fetchWeatherApi(city);
}

// Function to fetch weather data
async function fetchWeatherApi(city) {
  try {
    const cachedData = localStorage.getItem(city);

    if (cachedData) {
      const weatherData = JSON.parse(cachedData);
      getWeather(weatherData);
    } else {
      const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
      const weatherResponse = await fetch(weatherUrl);
      const weatherData = await weatherResponse.json();

      if (weatherData.cod === "404") {
        alertBox("City not found");
      } else {
        storeDataInLocalStorage(city, weatherData);
        getWeather(weatherData);
      }
    }
  } catch (error) {
    alertBox(`${error}`);
  }
}

// Function to store weather data in local storage
function storeDataInLocalStorage(city, data) {
  localStorage.setItem(city, JSON.stringify(data));
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
  const city = document.querySelector(".search-input").value;
  fetchWeatherApi(city);
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
  }, 2000);
}

// Waits for the HTML document to be fully loaded before executing the enclosed code.
document.addEventListener("DOMContentLoaded", function () {
  // When the icon is clicked, it calls search() function.
  document.getElementById("buttonClick").addEventListener("click", function () {
    search();

  });

  // When the "Enter" key is released, it calls search() function.
  document
    .querySelector(".search-input")
    .addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        search();
      }
    });

  fetchWeatherApi("Cullman");
});

document.addEventListener("DOMContentLoaded", function () {
  const cities = loadCitiesFromLocalStorage();
  if (cities.length > 0) {
    fetchWeatherApi(cities[0]);
  }
});
