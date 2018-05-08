
var pkname = document.getElementById('pklotname');
var pkID = document.getElementById('pklotID');
var pkresolution = document.getElementById('resolution');




$("#upload").click(function(){

    var form_data = new FormData();
    var files = $('#pklotImage')[0].files[0];
    form_data.append('file',files);

    var name = pkname.value; 
    var ID = pklotID.value;
    var resolution = pkresolution.value;

    $.ajax({
        url: 'newpklot.php',
        type: 'post',
        data: {
        	name: name,
        	ID: ID,
        	resolution: resolution
        },
        cache: false,
        success: function(data){
        	image_up(form_data);
        },
    });
});

function image_up(fdata){

	$.ajax({
        url: 'image.php',
        type: 'post',
        data: fdata,
        contentType: false,
        processData: false,
        success: function(response){
            alert(response);
            window.location.href = 'parkinglots.html';
        },
    });

}