<?php

header("Content-Type: application/json; charset=UTF-8");


$connect = mysqli_connect('localhost','sebRM','sebrm', 'Rumbomobile');


$sql = "SELECT * FROM Parkinglots";
$result = mysqli_query($connect, $sql);

$outp = "[";
while($rs = $result->fetch_assoc()) {
    if ($outp != "[") {$outp .= ",";}
    $outp .= '{"Name":"'  . $rs["Name"] . '",';
    $outp .= '"ID":"'   . $rs["ID"]        . '",';
    $outp .= '"Date":"'   . $rs["Date"]        . '",';
    $outp .= '"Resolution":"'. $rs["Resolution"]     . '"}'; 
}
$outp .="]";

echo ($outp);

?>