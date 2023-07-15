const apiKey = "fef8d2dffbb9e6b7136baacf21527fe9";
// const apiKey = "345752d369b66791e891af7fae98eb67";

async function fetchWeatherApi(city) {
  try {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
    const response = await fetch(url);
    const weatherData = await response.json();

    if (weatherData.cod === "404") {
      displayAlert("City not found", "#ff4d4d");
    } else {
      getWeather(weatherData);
    }

  } catch (error) {
    console.error("Error fetching weather data:", error);
  }
}

function getDate() {
  const today = new Date();
  const options = { weekday: "long", month: "long", day: "numeric" };
  return today.toLocaleDateString(undefined, options);
}

function getWeather(weatherData) {
  const { name } = weatherData;
  const currentDate = getDate();
  const { icon, description } = weatherData.weather[0];
  const { temp: temperature, humidity, pressure } = weatherData.main;
  const { speed: windSpeed } = weatherData.wind;

  displayWeather(
    name,
    icon,
    description,
    temperature,
    humidity,
    windSpeed,
    pressure,
    currentDate
  );
}

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
  document.querySelector(".city").innerText = name;
  document.querySelector(".temp").innerText = temperature + "°C";
  document.querySelector(".description").innerText =
    description.charAt(0).toUpperCase() + description.slice(1);
  document.querySelector(
    ".icon"
  ).src = `https://openweathermap.org/img/wn/${icon}.png`;
  document.querySelector(".humidity").innerText = `Humidity: ${humidity}%`;
  document.querySelector(".wind").innerText = `Wind Speed: ${windSpeed}km/hr`;
  document.querySelector(".pressure").innerText = `Pressure: ${pressure} pa`;
  document.querySelector(".date").innerText = currentDate;
}

function search() {
  fetchWeatherApi(document.querySelector(".search-input").value);
}


function changeBackgroundImage() {
  const randomNumber = Math.floor(Math.random() * 1000);
  document.body.style.backgroundImage = `url('https://source.unsplash.com/1920x1080/?nature&${randomNumber}')`;
}


function displayAlert(message, color) {
  const alertBox = document.createElement("div");
  alertBox.textContent = message;
  alertBox.classList.add("alert");
  alertBox.style.backgroundColor = color;
  document.body.insertBefore(alertBox, document.body.firstChild);

  setTimeout(function () {
    alertBox.remove();
  }, 3000);
}


document.addEventListener("DOMContentLoaded", function () {
  let clickedAction = document.getElementById("buttonClick");
  document.getElementById("buttonClick").addEventListener("click", function () {
    changeBackgroundImage();
    search();

  });

  document
    .querySelector(".search-input")
    .addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        search();
        changeBackgroundImage();
      }
    });

  fetchWeatherApi("Cullman");
  changeBackgroundImage();
});


