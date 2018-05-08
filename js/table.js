


$(document).ready(function(){
     $.ajax({
          url: "table.php",
          data: "",
          cache: false,
          dataType: 'json',
          success: function(data) {
            writetable(data);
          }
        });
});




function writetable(data){
    var arr = data;
    var i;
    var out = "<table>";

    out += "<tr><th>Parkinglot Name</th>";
    out += "<th>Parkinglot ID</th>";
    out += "<th>Creation Date</th>";
    out += "<th>Image Resolution</th></tr>";

    for(i = 0; i < arr.length; i++) {
        out += "<tr><td>" +
        arr[i].Name +
        "</td><td>" +
        arr[i].ID +
        "</td><td>" +
        arr[i].Date +
        "</td><td>" +
        arr[i].Resolution +
        "</td></tr>";
    }
    out += "</table>";
    document.getElementById("pklot-table").innerHTML = out;
}