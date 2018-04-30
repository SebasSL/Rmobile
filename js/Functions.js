

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
	$("canvas").css({"background-image": "url(images/Escenario1.jpg)"}); 
});
	
canvas.width = 1000;
canvas.height = 620;


canvas.addEventListener('mousedown', savecoord);

function savecoord(evt){
	if (stack < 4){
		Xpos = evt.pageX - canvas.offsetLeft - 210;
		Ypos = evt.pageY - canvas.offsetTop - 84;
		corners_X[stack] = Xpos;
		corners_Y[stack] = Ypos;
		context.fillStyle = "#CA0000";
		context.fillRect(Xpos,Ypos,4,4);
		stack = stack + 1;
	}else{
		alert("no puede dibujar mas de 4 puntos")
	}

}


function recreate(data){

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

function erase(){

	if (stack < 4){
		for (var i = 0; i <= 3 ; i++) {
			context.clearRect(corners_X[i],corners_Y[i],4,4);
		}
		stack = 0;
		corners_Y = [0,0,0,0];
		corners_X = [0,0,0,0];
	}else{
		tablename = "Parkinglot1"

		$.ajax({
	      url: "recreate.php",
	      method: "POST",
	      data: {
	      	tablename: tablename
	      },
	      cache: false,
	      success: function(data) {

	      	rec_data = $.parseJSON(data);
	      	console.log(rec_data[1][0])
	      	console.log(rec_data[0])
			context.clearRect(0, 0, canvas.width, canvas.height);

			recreate(rec_data);
	      }
	    });

	    stack = 0;
		corners_Y = [0,0,0,0];
		corners_X = [0,0,0,0];
		document.getElementById("ParkingID").value = 0;
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
	

	$.ajax({
      url: "data_up.php",
      method: "POST",
      data: {
      	ParkingID: id,
      	CoordX: corX,
      	CoordY: corY
      },
      cache: false,
      success: function(data) {

      	stack = 0;
		corners_Y = [0,0,0,0];
		corners_X = [0,0,0,0];
		document.getElementById("ParkingID").value = 0;

      }
    });
}

