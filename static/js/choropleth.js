let map = L.map("country-choro").setView([17.5707, -3.9932], 2);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

d3.json('/api/v1.0/geojson').then(function(geojsonData) {
    L.geoJson(geojsonData).addTo(map);
});

d3.json('/api/v1.0/geojson').then(geojsonData => console.log(geojsonData))

d3.json('/api/v1.0/amounts/countries/1992').then(data => console.log(data))


// adding color
function getColor(f) {
    return f > 1312500 ? '#800026' :
           f > 1125000 ? '#BD0026' :
           f > 937500 ? '#E31A1C' :
           f > 750000 ? '#FC4E2A' :
           f > 562500 ? '#FD8D3C' :
           f > 375000 ? '#FEB24C' :
           f > 187500 ? '#FED976' :
                      '#FFEDA0';
}
function style(feature) {
    return {
        fillColor: getColor(1000000),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

d3.json('/api/v1.0/geojson').then(function(geojsonData) {
    L.geoJson(geojsonData, {style: style}).addTo(map) 
});

// // Add style function so that fill layer depends on food production
// function style(feature, amountsData) {
//     console.log(feature);
//     console.log(`feature`);
//     console.log(amountsData);
//     console.log(`amountsData`);
//     let name = feature.properties.admin;
//     let amount = amountsData.countries[name];
//     return {
//         fillColor: getColor(1000000),
//         weight: 2,
//         opacity: 1,
//         color: 'white',
//         dashArray: '3',
//         fillOpacity: 0.7
//     };
// }
// d3.json('/api/v1.0/geojson').then(function(geojsonData) {
//     L.geoJson(geojsonData, style(feature, amountsData)).addTo(map)
//     d3.json('/api/v1.0/amounts/countries/1992').then(function(amountsData) {L.geoJson(geojsonData, style(feature, amountsData)).addTo(map)});
// })

// d3.json('/api/v1.0/amounts/countries/1992').then(function(amountsData) {
//     d3.json('/api/v1.0/geojson').then(function(geojsonData) {L.geoJson(geojsonData, style(feature, amountsData)).addTo(map)});
// })


// Add interaction
function highlightFeature(e) {
    let layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
}

let geojson;
// ... our listeners
d3.json('/api/v1.0/geojson').then(function(geojsonData) {
    geojson = L.geoJson(geojsonData, {
    style: style
    })
});

// Click listener that zooms to country on click
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

// Add listeners on countries layer
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

d3.json('/api/v1.0/geojson').then(function(geojsonData) {
    geojson = L.geoJson(geojsonData, {
    style: style,
    onEachFeature: onEachFeature
    }).addTo(map)
});

// Add info control
let info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h4>Food Availability</h4>' +  (props ?
        '<b>' + props.name + '</b><br />' + props.density + ' people / mi<sup>2</sup>'
        : 'Hover over a country');
};

info.addTo(map);

// Update legend when user hovers over country
function highlightFeature(e) {
    let layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }

    info.update(layer.feature.properties);
}

function resetHighlight(e) {
    geojson.resetStyle(e.target),
    info.update();
}

// Add legend control
let legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {

    let div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 187500, 375000, 562500, 750000, 937500, 1125000, 1312500],
        labels = [];

    // Loop through our food intervals and generate a label with a colored square for each interval
    for (let i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(map);