function lineChart(countryCode) {
    d3.json(`/api/v2.0/linechart/${countryCode}`).then(function (data) {
        let years = data.years;
        lineData = [{
            x: data.temperatures,
            y: data.amounts,
            text: years,
            type:"line"}];
        Plotly.newPlot("trend-line", lineData);   });   };

function color(amounts) {
    let total = amounts.reduce((par, amount) => par + amount, 0)
    return amounts.map(amount=>`rgb(100, 100, ${255/total*amount})`)   }

function pieChart(countryCode, year) {
    d3.json(`/api/v2.0/piechart/${countryCode}/${year}`).then(function (data) {
        let plotData = {
            labels: data.cetegories,
            datasets: [{
                label: `<h5>Types of Food</h5><br/>${year}`,
                backgroundColor: ['lightred', 'green', 'yellow', 'pink', 'lightblue', 'orange', 'purple','darkblue', 'darkred'],
                borderColor: 'black',
                data: data.amounts}]    };
            let myChart = new Chart(
                document.getElementById('pie-chart'),
                {type: 'pie', data: plotData, options: {}}   );   });   };

        // let pieData = [{
        //     values: data.amounts,
        //     labels: data.categories,
        //     type: "pie"}];
        // let layout = {
        //     height: 600,
        //     width: 800};
        // Plotly.newPlot("types-pie", pieData, layout);   });   

function pieYearChanged(year){
    let country = d3.select("#country").property("value");
    pieChart(country,year);   };

function countryChanged(country){
    lineChart(country);
    let year = d3.select("#pieYear").property("value");
    piechart(country, year);    }

function init() {
    // initialize the country selector dropdown
    let countrySelector = d3.select("#country");
    countrySelector.append("option").text("ALL COUNTRIES").property("value","sum");
    d3.json('/api/v2.0/countrieslist').then(data => {
        let country_codes = data.country_codes;
        let country_names = data.country_names;
        for (let i=0 ; i<country_codes.length; i++) {
            let country_code = country_codes[i]
            let country_name = country_names[i]
            countrySelector.append("option").text(country_name).property("value", country_code);   };
        let country = countrySelector.property("value");
        lineChart(country);   });

    // initialize the year selector dropdown
    let yearSelector = d3.select("#pieYear");
    let years = [...Array(22).keys()].map(e=>e+1992);
    for(let i=0 ; i<years.length; i++){
        let year = years[i];
        yearSelector.append("option").text(year).property("value", year);    };
    let year = yearSelector.property("value");
    let countryCode = d3.select('#country').property('value');
    pieChart(countryCode, year);    };
     
init();