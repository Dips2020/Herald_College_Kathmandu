<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

// $host = "sql301.infinityfree.com";
// $username = "if0_34836583";
// $password = "2xS6EaE8Ex";
// $dbname = "if0_34836583_weathers";
$host = "localhost";
$username = "root";
$password = "";
$dbname = "weathers";

// Create connection
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Receive data from JavaScript
$data = json_decode(file_get_contents('php://input'), true);


$city = $data['city'];
$temperature = $data['temperature'];
$description = $data['description'];
$date = $data['date'];
$day_of_week = $data['day_of_week'];
$icon = $data['icon'];




// Get current date in YYYY-MM-DD format
$currentDate = date('Y-m-d');

// Check if data for the same date and city already exists
$checkQuery = "SELECT * FROM weather_data WHERE date = '$date' AND city = '$city' LIMIT 1";
$checkResult = $conn->query($checkQuery);

if ($checkResult->num_rows === 0) {
    // Insert data into the database
    $insertQuery = "INSERT INTO weather_data (city, temperature, description, date, day_of_week, icon) 
                    VALUES ('$city', '$temperature', '$description', '$date', '$day_of_week','$icon')";

    if ($conn->query($insertQuery) === TRUE) {
        echo "Data inserted successfully";
    } else {
        echo "Error: " . $insertQuery . "<br>" . $conn->error;
    }
} else {
    echo "Data for the same date and city already exists.";
}


$conn->close();
?>