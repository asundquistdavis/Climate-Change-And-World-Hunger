function barChart(data) {
    let sorted = [];
    for (var country in data['countries']) {
        sorted.push([country, data['countries'][country]]);     };
    sorted.sort(function(a, b) {return a[1]-b[1]});
    let barData = {
        x: sorted.map(pair=>pair[1]).slice(sorted.length-10, sorted.length),
        y: sorted.map(pair=>pair[0]).slice(sorted.length-10, sorted.length),
        type: 'bar',
        orientation: 'h'    };
    let barLayout = {
        margin: {l: 0, r: 0, b: 30, t: 0}    };
    Plotly.newPlot('top-bar', [barData], barLayout);   };

d3.json('/api/v1.0/amounts/countries/2013').then(data => barChart(data));