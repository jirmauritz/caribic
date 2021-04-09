// show connection status
var connDiv = $('#connected')[0];
var disconnDiv = $('#disconnected')[0];

socket.on('connect', function() {
        connDiv.style.display = "block";
        disconnDiv.style.display = null;
      })

socket.on('disconnect', function() {
        connDiv.style.display = null;
        disconnDiv.style.display = "block";
      })