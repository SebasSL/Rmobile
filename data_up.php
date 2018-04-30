<?php
$connect = mysqli_connect('localhost','sebRM','sebrm', 'Rumbomobile');


$ID = $_POST["ParkingID"];
$coordX = $_POST["CoordX"];
$coordY = $_POST["CoordY"];

$sqli= "INSERT INTO `Parkinglot1`(`ID`, `CoordX`, `CoordY`) VALUES ( '".$ID."' , '".$coordX."' , '".$coordY."')";
mysqli_query($connect, $sqli);
echo $coordX;
?>