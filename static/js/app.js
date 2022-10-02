// request data from api
async function getTemps() {
    let temps = await d3.json('/api/v1.0/temps');
};

async function executeChoropleth() {
    let foods =  await d3.json('/api/v1.0/foods');
};


// populate #year-select



// populate #country-select



// render chloropleth



// render markers map



// render line chart
