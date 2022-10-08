let map = L.map("country-choro").setView([37.8, -96], 1);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

d3.json('/api/v1.0/geojson').then(function(geojsonData) {
    L.geoJson(geojsonData).addTo(map);
});

d3.json('/api/v1.0/geojson').then(geojsonData => console.log(geojsonData))