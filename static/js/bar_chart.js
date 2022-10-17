function barChart(year) {
    d3.json(`/api/v2.0/barchart/${year}`).then(data => {
        let barData = {
            x: data.amounts.reverse(),
            y: data.country_names.reverse(),
            type: 'bar',
            orientation: 'h',
            text: data.country_names    };
        let barLayout = {
            margin: {l: 0, r: 0, b: 30, t: 0}    };
        Plotly.newPlot('top-bar', [barData], barLayout);   });   };