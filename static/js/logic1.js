// Anjali's plotting functions
//function for populations";
// console.log("Lets Start plot population");
function populationPlot(country) {

	let url_all = `/population_all/${country}`; 
  d3.json(url_all).then(function(response) {
    // console.log(response);
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
      name: "Male PoPulation",
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
      title: "Population For " + country + " (in thousands)",
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

// console.log("Lets Start plot2");
function agePlot(country,year) {

	let url_all = `/age_group/${country}/${year}`; 
  d3.json(url_all).then(function(response) {
    // console.log(response);
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
			title: "Population by Age Group (in thousands)",
		};
		

    Plotly.newPlot("population-stack", data, layout);
  });
}

