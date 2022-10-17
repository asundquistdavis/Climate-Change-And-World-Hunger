// Declare global variables
let years = [...Array(22).keys()].map(e=>e+1992)
let map;
let geojson;
let amountsData;
let legend;
let info;

// function that fetches food aount for given country code 
function getAmount(country_code, data) {
    let i = data.country_codes.indexOf(country_code)
    return data.amounts[i]
}

// function to add color based on food amount
function getColor(f) {
    return f > 20000 ? '#006837' :
            f > 15000 ? '#1a9850' :
            f > 10000 ? '#66bd63' :
            f > 5000 ? '#a6d96a' :
            f > 2500 ? '#d9ef8b' :
            f > 1000 ? '#ffffbf' :
            f > 750 ? '#fee08b' :
            f > 500 ? '#fdae61' :
            f > 100 ? '#f46d43' :
            f > 50 ? '#d73027' :
            f >= 0 ? '#a50026' :
            '#aaaaaa'}

// function to color on total food amount
function style(feature) {
    return {
        fillColor: getColor(getAmount(feature.properties.ISO_A3, amountsData)),
        weight: 1,
        opacity: 1,
        color: 'black',
        dashArray: '3',
        fillOpacity: 0.6    };  }

// funtion to highlight country and to reset
function highlightFeature(e) {
    let layer = e.target;
    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.6    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();   }  
    
    info.update(layer.feature.properties);
    }

function resetHighlight(e) {
    geojson.resetStyle(e.target);   
    info.update()   }

// Click listener that zooms to country on click
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());    }

// Add listeners on countries layer
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature});  }


// Create choropleth function to be called at various years
function choropleth(year) {

    // Reset existing style layer before applying a new one
    if(geojson) {
        map.removeLayer(geojson)
      };

    // Draw the style layer  
    d3.json(`/api/v2.0/choropleth/amounts/${year}`).then(function(data) {
        amountsData = data
        d3.json(`/api/v2.0/choropleth/geo`).then(function(geoData) {
            geojson = L.geoJson(geoData, {
                style: style,
                onEachFeature: onEachFeature})
                .addTo(map)   });   });

    // Add legend control
    if(legend instanceof L.Control) {
        map.removeControl(legend);
    }

    legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        let div = L.DomUtil.create('div', 'info legend'),
            grades = [0, 50, 100, 500, 750, 1000, 2500, 5000, 10000, 15000, 20000],
            labels = [];

        // Loop through our food intervals and generate a label with a colored square for each interval
        for (let i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };

    info.addTo(map);
    legend.addTo(map);  }

// function to update choroplet on year change
function choroplethYearChanged(year) {
    barChart(year)
    choropleth(year);   }

// function to initialize the choropleth
function init() {
    // add base layer
    map = L.map("country-choro").setView([17.5707, -3.9932], 3);

    // add tile layer
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'})
    .addTo(map);

    // add info layer
    if(info instanceof L.Control) {
        map.removeControl(info);} 

    info = L.control();

    info.update = function (props) {
        this._div.innerHTML = '<h4>Food Availability</h4>' +  (props ?
            '<b>' + props.ADMIN + '</b><br/>' + ((amount = getAmount(props.ISO_A3, amountsData)) ? amount + ' millions of tons' : 'No data available')
            : 'Hover over a country');
    };

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;   };

    // poplulate dropdown selector
    let selector = d3.select("#choroplethYear");
    for (let i=0 ; i<years.length;i++) {
        let year = years[i]
        selector.append("option").text(year).property("value",year);    };

    // draw style layer with initial year option
    let initialyear = selector.property("value");
    barChart(initialyear)
    choropleth(initialyear);    };

init();
