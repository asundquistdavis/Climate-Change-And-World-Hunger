// // use this call to get geojson data...
// d3.json('/api/v1.0/geojson').then(geojsonData => console.log(geojsonData))

// // use this call to get amounts data by year summed over all country_codes, both types and all categpries...
// d3.json('/api/v1.0/amounts').then(amountsData=>console.log(amountsData))

// // use this call to get amounts data by year and category - type can be either ['Food' or 'Feed'] and if country_code == 'sum' then summed over all countries...
// // country_code must be uppercase ISO_3 or 'sum'.   
//d3.json('/api/v1.0/amounts/AFG/Feed').then(amountsData=>console.log(amountsData))

// // use this call to get temperatures data...
//d3.json('/api/v1.0/temperatures').then(temperaturesData=>console.log(temperaturesData))

console.log("This is app.js");

function linegraph(){

    d3.json('/api/v1.0/temperatures').then(temperaturesData=>{console.log(temperaturesData)
        let years = Object.keys(temperaturesData.years);
        console.log(years);
        let temperatures = Object.keys(temperaturesData.years).map(year=>temperaturesData.years[year].tempurature);
        console.log(temperatures);
        d3.json('/api/v1.0/amounts').then(amountsData=>{console.log(amountsData)
            let amounts = Object.keys(amountsData.years).map(year=>amountsData.years[year]);
            console.log(amounts);

            lineData = {
                   x:temperatures,
                   y:amounts,
                   text:years,
                   type:"line"


            }
            Plotly.newPlot("trend-line",[lineData] );

    
        });
    

    });

    

}

linegraph();

function piechart(country, year){
    d3.json(`/api/v1.0/amounts/${country}/Food`).then(function(amountsData){console.log(amountsData)
        let categories = Object.keys(amountsData.years[year]);
        console.log(categories);
        let amounts = categories.map(category=>amountsData.years[year][category]);
        console.log(amounts);

        let data = [{
            values: amounts,
            labels: categories,
            type: "pie"
          }];
        
          let layout = {
            height: 600,
            width: 800
          };
        
          Plotly.newPlot("types-pie", data, layout);
    
    });
         

}
piechart("AFG",2013);

// function piechartchanged(year){

//      let country = "AFG";
//      piechart(country,year);




// }

function pieyearchanged(year){
    piechart("AFG",year);
}

function InitDashboard() 
{
       console.log('InitDashboard()');

       //Initialize the dropdown
        //let selector = d3.select("#pieyear").innerHTML;
        let selector = d3.select("#pieyear");

      // Get a handle to the dropdown
      d3.json('/api/v1.0/temperatures').then(temperaturesData=>{console.log(temperaturesData)

            
            let years = Object.keys(temperaturesData.years);
            // let list=years.map(year=>`<option>${year}</option>`);
            console.log(years);
            // for(let year=years[0];year<years.length;year++){

            //     list.push(`<option>${year}</option>`)

            // }
            // console.log(`list: ${list}`);
            // selector = list.join();
            for(let i=0 ; i<years.length;i++){

                let year = years[i]
                selector.append("option").text(year).property("value",year);
            };
            let initialyear = selector.property("value");

            piechart(initialyear);


       });
    



 }

InitDashboard();

function country(data){
        

}