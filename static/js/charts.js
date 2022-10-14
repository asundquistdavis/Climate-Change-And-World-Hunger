// // use this call to get geojson data...
// d3.json('/api/v1.0/geojson').then(geojsonData => console.log(geojsonData))

// // use this call to get amounts data by year summed over all country_codes, both types and all categpries...
// d3.json('/api/v1.0/amounts').then(amountsData=>console.log(amountsData))

// // use this call to get amounts data by year and category - type can be either ['Food' or 'Feed'] and if country_code == 'sum' then summed over all countries...
// // country_code must be uppercase ISO_3 or 'sum'.   
//d3.json('/api/v1.0/amounts/AFG/Feed').then(amountsData=>console.log(amountsData))

// // use this call to get temperatures data...
//d3.json('/api/v1.0/temperatures').then(temperaturesData=>console.log(temperaturesData))



function linegraph(country){

    d3.json('/api/v1.0/temperatures').then(temperaturesData=>{console.log(temperaturesData)
        let years = Object.keys(temperaturesData.years);
        console.log(years);
        let temperatures = Object.keys(temperaturesData.years).map(year=>temperaturesData.years[year].temperature);
        console.log(temperatures);
        
        try{
            d3.json(`/api/v1.0/amounts/${country}`).then(amountsData=>{console.log(amountsData)
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

        }
        catch(error) {
            console.log(error);
            d3.select('#trend-line').text("No data available for the selected country, please select another country.")
        }
       
    
        });
    

 

    

}



function piechart(country, year){
    d3.json(`/api/v1.0/amounts/years/${country}/Food`).then(function(amountsData){console.log(amountsData)
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


function pieyearchanged(year){
    let country = d3.select("#selDataset").property("value");
    piechart(country,year);
}

function InitDashboard() 
{
       console.log('InitDashboard()');

       //Initialize the dropdown
        
        let selector = d3.select("#pieyear");

      // Get a handle to the dropdown
      d3.json('/api/v1.0/temperatures').then(temperaturesData=>{console.log(temperaturesData)

            
            let years = Object.keys(temperaturesData.years);
           
            console.log(years);
            
            for(let i=0 ; i<years.length;i++){

                let year = years[i]
                selector.append("option").text(year).property("value",year);
            };
            let initialyear = selector.property("value");

            piechart("AFG",initialyear);


       });
    



 }

InitDashboard();

function optionChanged(country){
    linegraph(country);
    let year = d3.select("#pieyear").property("value");
    piechart(country,year);

}


function country(){

    //Initialize the dropdown
       
        let selector = d3.select("#selDataset");

        selector.append("option").text("ALL COUNTRIES").property("value","sum");

      // Get a handle to the dropdown
      d3.json('/api/v1.0/amounts/countries/2013').then(geojson=>{console.log(geojson)

            
            let countries = Object.keys(geojson.countries) ;  
            // let codes = (geojson.features.map(feature=>feature.properties.ISO_A3));
            
            console.log(countries);
            
            for(let i=0 ; i<countries.length;i++){

                let country = countries[i]
                // let code = codes[i]
                selector.append("option").text(country).property("value",country);
            };
            let initialcountry = selector.property("value");

            
            linegraph(initialcountry);


       });
        

}
country();