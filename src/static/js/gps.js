// init sockerIO
var socket = io();

var map = L.map('mapid').setView([50.0996211, 14.581498], 18);

var boatIcon = L.icon({
    iconUrl: 'static/img/marker_boat.png',
    iconSize:     [10, 30], // size of the icon
    iconAnchor:   [5, 15], // point of the icon which will correspond to marker's location
});

var offlineLayer = L.tileLayer('/static/tiles/{z}/{x}/{y}.png', {
    minZoom: 18,
    maxZoom: 19,
    maxNativeZoom:18,
    iconUrl: 'img/marker_boat.png'
}).addTo(map);

var marker = L.marker([50.0996211, 14.581498], {icon: boatIcon}).addTo(map);

var btn = $('#btn')[0];
btn.onclick = function() {
    socket.emit('btn', 0);
};

socket.on("location", (satellites, lat, lng) => {
  marker.setLatLng(new L.LatLng(lat, lng));
});