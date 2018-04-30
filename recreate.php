<?php
$connect = mysqli_connect('localhost','sebRM','sebrm', 'Rumbomobile');


//$table = $_POST["tablename"];

$ID = [];
$coordx = [];
$coordy =  [];


$table = "Parkinglot1";

$sql= "SELECT count(ID) FROM `".$table."`";
$result = mysqli_query($connect, $sql);
$row = mysqli_fetch_array($result,MYSQLI_ASSOC);

$num_rows = $row["count(ID)"];

$sqli= "SELECT * FROM `".$table."`";
$result = mysqli_query($connect, $sqli);
//$row = mysqli_fetch_array($result,MYSQLI_ASSOC);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $ID[]=$row["ID"];
        $coordx[]=$row["CoordX"];
        $coordy[]=$row["CoordY"]; 
    }
}
echo json_encode(array($ID,$coordx,$coordy));

?>