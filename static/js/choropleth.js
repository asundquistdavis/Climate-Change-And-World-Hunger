// Add choropleth with dropdown to page

// Add base layer
let map = L.map("country-choro").setView([17.5707, -3.9932], 3);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

d3.json('/api/v2.0/choropleth/1992').then(function(geojsonData) {
    L.geoJson(geojsonData).addTo(map);
});

// Declare global variables
let legend;
let info;

// Create choropleth function to be called at various years
function choropleth(year) {

    // Create getColor function to add color
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
                    '#a50026' ;
    }

    // Create style function to color on total food amount
    function style(feature) {
        return {
            fillColor: getColor(feature.properties.amount),
            weight: 1,
            opacity: 1,
            color: 'black',
            dashArray: '3',
            fillOpacity: 0.7
        };
    }

    // Add interaction

    // Create funtion to highlight country and to reset
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

    d3.json(`/api/v2.0/choropleth/${year}`).then(function(geojsonData) {
        geojson = L.geoJson(geojsonData, {
        style: style,
        onEachFeature: onEachFeature
        }).addTo(map)
    });

    // Add info control
    if(info instanceof L.Control) {
        map.removeControl(info);
    }
    info = L.control();

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;
    };

    // Method that we will use to update the control based on feature properties passed
    info.update = function (props) {
        this._div.innerHTML = '<h4>Food Availability</h4>' +  (props ?
            '<b>' + props.ADMIN + '</b><br />' + props.amount + " millions of tons</sup>"
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

    legend.addTo(map);
}

// Function to update choroplet on year change
function choroplethyearchanged(year){
    choropleth(year);
}

function InitDashboard() 
{
       console.log('InitDashboard()');

       //Initialize the dropdown
       
        let selector = d3.select("#choroplethyear");

      // Get a handle to the dropdown
      d3.json('/api/v1.0/temperatures').then(temperaturesData=>{console.log(temperaturesData)

            
            let years = Object.keys(temperaturesData.years);
          
            for(let i=0 ; i<years.length;i++){

                let year = years[i]
                selector.append("option").text(year).property("value",year);
            };
            let initialyear = selector.property("value");

            choropleth(initialyear);
        

       });
    
 }

InitDashboard();
