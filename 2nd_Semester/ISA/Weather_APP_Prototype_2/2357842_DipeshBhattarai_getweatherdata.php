<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "weathers";

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$data = array();

$sql = "SELECT `description`, `temperature`,  `city`, `date`, `day_of_week`, `icon` FROM `weather_data` WHERE `city` = 'Cullman' ORDER BY `id` DESC LIMIT 7";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
}

$conn->close();
header('Content-Type: application/json');
echo json_encode($data);
?>