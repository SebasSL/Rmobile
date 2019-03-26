

var draw_button = document.getElementById('draw');
var save_button = document.getElementById('save');
save_button.style.display = "none";
var canvas = document.getElementById('Parking');
var context = canvas.getContext('2d');
context.lineWidth = 2;
corners_X = [0,0,0,0];
corners_Y = [0,0,0,0]; 
stack = 0;
start_X = 0;
start_Y = 0; 
var i;
var j;
var id = 0;
var corX;
var corY;
var test = 4;
var rec_data;
var tablename;
var rawcoordsX;
var rawcoordsY;

$(document).ready(function(){
	var queryString = decodeURIComponent(window.location.search);
	queryString = queryString.substring(4);
	$.ajax({
      url: "initdata.php",
      method: "POST",
      data: {
      	ParkingID: queryString
      },
      cache: false,
      success: function(data) {
      	init_data = $.parseJSON(data);
      	setcanvas(init_data)
      }
    });
});

function setcanvas(data){

	$("canvas").css({"background-image": "url(images/init_images/"+data[2]+")"}); 
	var res = data[1].split(",");
	canvas.width = res[0];
	canvas.height = res[1];
	tablename = data[0];
	document.getElementById("pktitle").innerHTML = data[0];
	recreate();
}

canvas.addEventListener('mousedown', savecoord);

function savecoord(evt){
	if (stack < 4){
		Xpos = evt.pageX - canvas.offsetLeft - 227;
		Ypos = evt.pageY - canvas.offsetTop - 94;
		corners_X[stack] = Xpos;
		corners_Y[stack] = Ypos;
		context.fillStyle = "#CA0000";
		context.fillRect(Xpos,Ypos,4,4);
		stack = stack + 1;
	}else{
		alert("no puede dibujar mas de 4 puntos")
	}

}


function recreate(){
	
	$.ajax({
      url: "recreate.php",
      method: "POST",
      data: {
      	tablename: tablename
      },
      cache: false,
      success: function(rawdata) {

      	data = $.parseJSON(rawdata);
		
		for (var k = 0; k < data[0].length; k++){

			rawcoordsX = data[1][k].split(",");
			rawcoordsY = data[2][k].split(",");

			for (var j = 0; j <= 3; j++){
					
				start_X = parseInt(rawcoordsX[j]);
				start_Y = parseInt(rawcoordsY[j]);

				for (var i = 0; i <= 3-j ; i++) {

					context.beginPath();
					context.moveTo(start_X , start_Y);
					context.lineTo(parseInt(rawcoordsX[i+j]),parseInt(rawcoordsY[i+j]));
					context.strokeStyle = "#FF0000";
					context.stroke();
				
				}
			}
		}
      }
    });
	
	draw_button.style.display = "block";
	save_button.style.display = "none";
}

function erase(){

	if (stack < 4){
		for (var i = 0; i <= 3 ; i++) {
			context.clearRect(corners_X[i],corners_Y[i],4,4);
		}
		stack = 0;
		corners_Y = [0,0,0,0];
		corners_X = [0,0,0,0];
	}else{
		
	    stack = 0;
		corners_Y = [0,0,0,0];
		corners_X = [0,0,0,0];
		document.getElementById("ParkingID").value = 0;
		context.clearRect(0, 0, canvas.width, canvas.height);
		recreate();
	}
}



function draw(){

	id = document.getElementById("ParkingID").value;


	if (stack == 4 && id != 0){
		
		for (var j = 0; j <= 3; j++){
			
			start_X = corners_X[j];
			start_Y = corners_Y[j];

			for (var i = 0; i <= 3-j ; i++) {

				context.beginPath();
				context.moveTo(start_X , start_Y);
				context.lineTo(corners_X[i+j],corners_Y[i+j]);
				context.strokeStyle = "#FF0000";
				context.stroke();
			
			}
		}
		console.log(id)
		console.log(corners_X)
		console.log(corners_Y)

		draw_button.style.display = "none";
		save_button.style.display = "block";
		
		
	}else{
		
		alert("Por favor marcar 4 puntos y escribir el numero de ID del parqueadero");	

	}


}

function updata(){

	corX = corners_X[0].toString();
	corY = corners_Y[0].toString();

	for (i = 1; i <= 3 ; i++){
		corX = corX.concat(",");
		corX = corX.concat(corners_X[i].toString());
		corY = corY.concat(",");
		corY = corY.concat(corners_Y[i].toString());
		console.log(corX)
	}
	
	alert(tablename)
	$.ajax({
      url: "data_up.php",
      method: "POST",
      data: {
      	ParkingID: id,
      	CoordX: corX,
      	CoordY: corY,
      	tablename: tablename
      },
      cache: false,
      success: function(data) {

      	stack = 0;
		corners_Y = [0,0,0,0];
		corners_X = [0,0,0,0];
		document.getElementById("ParkingID").value = 0;
		draw_button.style.display = "block";
		save_button.style.display = "none";


      }
    });
}

