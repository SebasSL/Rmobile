<?php

$connect = mysqli_connect('localhost','sebRM','sebrm', 'Rumbomobile');


$name       = $_POST["name"];
$ID         = $_POST["ID"];
$resolution = $_POST["resolution"];
$output = "";

$table_name = $name.$ID;

//Crear tabla
$sql = "CREATE TABLE ".$table_name." ( ID INT(6) UNSIGNED PRIMARY KEY, CoordX VARCHAR(30) NOT NULL, CoordY VARCHAR(30) NOT NULL)";
mysqli_query($connect, $sql);

$sqli = "INSERT INTO `Parkinglots`(`ID`, `Name`, `Resolution`, `Date` ) VALUES ( '".$ID."' , '".$name."' , '".$resolution."', NOW())";
mysqli_query($connect, $sqli);

echo $output;


?>