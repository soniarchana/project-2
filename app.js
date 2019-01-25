// Function to display world info in the panel

function worldInfo() {
  let panel = d3.select("#country-metadata");
  panel.html("");
  let div = panel.append("div");
  div.append("span").attr("class", "world-info").text(`Total Population:`);
  div.append("span").text(`7,383,009,000`);

  div.append("span").attr("class", "world-info").text(`Famale Population:`);
  div.append("span").text(`3,658,877,000`);

  div.append("span").attr("class", "world-info").text(`Male Population:`);
  div.append("span").text(`3,724,132,000`);   
}


//function for populations";
console.log("Lets Start plot population");
function populationPlot(country) {

	let url_all = `/population_all/${country}`; 
  d3.json(url_all).then(function(response) {
    console.log(response);
    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: "All Population",
      x: response.map(data => data.Year),
      y: response.map(data => data.A_Population),
      line: {
        color: "blue"
      }
		};
		
    var trace2= {
      type: "scatter",
      mode: "lines",
      name: "Male PoPulation ",
      x: response.map(data => data.Year),
      y: response.map(data => data.m_Population),
      line: {
        color: "red"
      }
		};
		

		var trace3= {
      type: "scatter",
      mode: "lines",
      name: "Female PoPulation ",
      x: response.map(data => data.Year),
      y: response.map(data => data.f_Population),
      line: {
        color: "green"
      }
    };
    var data = [trace1,trace2,trace3];

    var layout = {
      title: "Population For " + country,
      xaxis: {
				type: "date",
				title: "Years"
      },
      yaxis: {
        autorange: true,
				type: "linear",
				title: "Population numbers"
      }
    };
		

    Plotly.newPlot("population-line", data, layout);
  });
}

// function to plot population by age group

console.log("Lets Start plot2");
function agePlot(country,year) {

	let url_all = `/age_group/${country}/${year}`; 
  d3.json(url_all).then(function(response) {
    console.log(response);
    var trace1 = {
      type: "bar",
      name: "All Population",
      x: response.map(data => data.Year),
      y: response.map(data => data.A_Population),

		};

		var trace1 = {
			x: response.map(data => data.Age_Group),
			y: response.map(data => data.A_Population),
			name: 'all',
			type: 'bar'
		 };
		
		 var trace2 = {
			x: response.map(data => data.Age_Group),
			y: response.map(data => data.M_Population),
			name: 'male',
			type: 'bar'
		 };

		 var trace3 = {
			x: response.map(data => data.Age_Group),
			y: response.map(data => data.F_Population),
			name: 'female',
			type: 'bar'
		 };
    var data = [trace1,trace2,trace3];

		var layout = {
			barmode: 'stack',
			title: "Population by Age Group",
		};
		

    Plotly.newPlot("population-stack", data, layout);
  });
}


// Function to display world info in the panel
function countryInfo(country) {
  let url = `/country_info/${country}`; 

  d3.json(url).then(function(data) {

    // Select the panel with id of `#country-metadata`
    let panel = d3.select("#country-metadata");

    // Clear any existing metadata
    panel.html("");

    let div = panel.append("div");
    Object.entries(data).forEach(function([key, value]) {
      if (!value) {
        div.append("p").text(`${key}: N/A`);
      } else {
        div.append("span").attr("class", "world-info").text(`${key}: `);
        div.append("span").text(`${value}`);
      }     
    });
  });
}


// // Function to display world info in the panel
// function countryInfo(country) {
//   let url = `/country_info/${country}`; 

//   d3.json(url).then(function(data) {

//     // Select the panel with id of `#country-metadata`
//     let panel = d3.select("#country-metadata");

//     // Clear any existing metadata
//     panel.html("");

//     let div = panel.append("div");
//     Object.entries(data).forEach(function([key, value]) {
//       if (!value) {
//         div.append("p").text(`${key}: N/A`);
//       } else {
//         div.append("p").text(`${key}: ${value}`);
//       }     
//     });
//   });
// }


// Function to initilize the page
function init() {

	var selector = d3.select("#selCountry");
	var selector2 = d3.select("#selYear");
	
	d3.json("/countries").then((data) => {

		data.countries.forEach((country) => {
			selector
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
    const world = countries[0];
    worldInfo();
    populationPlot("WORLD")
		agePlot("WORLD",2015)

    // Add all build chart function here here:
    // buildCharts(world);
    // buildMetadata(world);
	});
}


// Function to build new charts when select a country
function optionChanged(newCountry) {

  // buildCharts(newSample);
  if (newCountry === "WORLD") {
  	worldInfo();
  } else {
    countryInfo(newCountry);
		populationPlot(newCountry);
		agePlot(newCountry,2010)
  }

}


init();
