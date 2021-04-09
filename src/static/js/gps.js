var map = L.map('mapid').setView([50.0996211, 14.581498], 19);


var offlineLayer = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: 'abc',
    minZoom: 19,
    maxZoom: 19,
    crossOrigin: false
}).addTo(map);