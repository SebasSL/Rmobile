<?php
$connect = mysqli_connect('localhost','Sebrm','Io274as', 'Rumbomobile');

$ID = $_POST["ParkingID"];
//$ID = 1;

$sql= "SELECT Name,Resolution,Format FROM Parkinglots WHERE ID = '".$ID."'";
$result = mysqli_query($connect, $sql);

$row = mysqli_fetch_array($result,MYSQLI_ASSOC);

$format = $row["Format"];
$Name = $row["Name"];
$Resolution = $row["Resolution"]; 
$image = $Name."_".$ID.".".$format;
$Name = $Name.$ID;

echo json_encode(array($Name,$Resolution,$image));

?>