
// // use this call to get geojson data...
// d3.json('/api/v1.0/geojson').then(geojsonData => console.log(geojsonData))

// // use this call to get amounts data by year summed over all country_codes, both types and all categpries...
// d3.json('/api/v1.0/amounts').then(amountsData=>console.log(amountsData))

// d3.json('/api/v1.0/amounts/1992').then(data=>console.log(data))

// // use this call to get amounts data by year and category - type can be either ['Food' or 'Feed'] and if country_code == 'sum' then summed over all countries...
// //country_code must be uppercase ISO_3 or 'sum'.   
// d3.json('/api/v1.0/amounts/AFG/Food').then(amountsData=>console.log(amountsData))

// // use this call to get temperatures data...
// d3.json('/api/v1.0/temperatures').then(temperaturesData=>console.log(temperaturesData))