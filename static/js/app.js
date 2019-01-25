// Function to initilize the page
function init() {

	var selector1 = d3.select("#selCountry");
	var selector2 = d3.select("#selYear");
	
	d3.json("/countries").then((data) => {

		data.countries.forEach((country) => {
			selector1
				.append("option")
				.text(country)
				.property("value", country);
	
		});

		data.years_bin.forEach((year) => {
			selector2
				.append("option")
				.text(year)
				.property("value", year);
	
		});

		// Use the first country from the list to build the initial plots
    const world = data.countries[0];
 
    mapPlot(1950);
    worldInfo('1950');
    populationPlot("WORLD");
		agePlot("WORLD",1950);
		topTenPlot(1950);
		growthRatePlot(1950);
	});
}


// Function to build new charts when select a country
function optionChanged(newCountry) {
  // year = d3.select;
  year = '1950';
  // buildCharts(newSample);
  if (newCountry === "WORLD") {
  	worldInfo(year);
  } else {
    countryInfo(newCountry);
		populationPlot(newCountry);
		agePlot(newCountry,2010)
  }
}


// Function to build new charts when select year
function optionChangedYear(year) {
  mapPlot(year);
  worldInfo(year);
  topTenPlot(year);
  growthRatePlot(year);
}

init();
