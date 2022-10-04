// request data from api
async function getTemps() {
    let temps = await d3.json('/api/v1.0/temps');
};

async function executeChoropleth() {
    let foods =  await d3.json('/api/v1.0/foods');
};


// #trend-line ... Country Food avail. vs World temps: Plotly line chart + select country drop down
// data set 1: total amount of food and feed in 1000 tonnes available  givin country by year
// data set 2: global world temperature in deg C by year

// #types-pie ... Types of food avail. by country: Plotly pie chart + select country drop down + select year
// data set 1: amount of food or feed available for each food type fo amount

// #country-choro ... Country food avail. 'health': Leaflet + choropleth - world map. Choropleth uses 'health' score which is computed using food and feed avail. 

// #top-bar ... Top producing conties: Ploty bar chart

// #bot-bar ... Bottom producing conties: Ploty bar chart
