<?php

$connect = mysqli_connect('localhost','Sebrm','Io274as', 'Rumbomobile');

$sql = "SELECT Name,ID FROM Parkinglots ORDER BY Date DESC";
$result = mysqli_query($connect, $sql);
$row = mysqli_fetch_array($result,MYSQLI_ASSOC);

$name = $row["Name"];
$ID = $row["ID"];


/* Getting file name */
$filename = $_FILES['file']['name'];

/* Location */
$location = "images/init_images/".$filename;
$uploadOk = 1;
$imageFileType = pathinfo($location,PATHINFO_EXTENSION);

// Check image format
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
 && $imageFileType != "gif" ) {
 $uploadOk = 0;
}

$sql = "UPDATE `Parkinglots` SET `Format` = '".$imageFileType."' WHERE `Parkinglots`.`ID` ='".$ID."'";
mysqli_query($connect, $sql);


if($uploadOk == 0){
 echo 0;
}else{
 /* Upload file */
 $location = "images/init_images/".$name."_".$ID.".".$imageFileType;
 
 if(move_uploaded_file($_FILES['file']['tmp_name'],$location)){
 echo $filename." was succesfully added";
 }else{
 echo "file was not uploaded";
 }
}

?>