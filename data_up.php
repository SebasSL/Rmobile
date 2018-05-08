<?php
$connect = mysqli_connect('localhost','sebRM','sebrm', 'Rumbomobile');


$ID = $_POST["ParkingID"];
$coordX = $_POST["CoordX"];
$coordY = $_POST["CoordY"];
$tablename = $_POST["tablename"];

$sqli= "INSERT INTO `".$tablename."`(`ID`, `CoordX`, `CoordY`) VALUES ( '".$ID."' , '".$coordX."' , '".$coordY."')";
mysqli_query($connect, $sqli);
echo $coordX;
?>