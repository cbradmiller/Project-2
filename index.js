var foodYears = [1990, 1995, 2000, 2005, 2010, 2015];
//maybe I should get these dynamically, but here they are without that.
var healthYears = [1991,1992,1993,1994,1995,1996,1997,
    1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,
    2008,2009,2010,2011,2012,2013,2014]

//Page setup

//first call the api to get the country names and set that part up
var baseURL = 'https://learning-heroku-ido.herokuapp.com'
var USHCURL = '/api/v1.0/USHealthCare'
var cnameURL = '/api/v1.0/countrynames'
var foodIURL = '/api/v1.0/dataFoodIndex'
var base_country_food_data = '/api/v1.0/foodData/' //and then the country name
var starting_country =	"USA, Puerto Rico and US Virgin Islands"

//setting up the page.
d3.json(baseURL + cnameURL , function(data){
    console.log(data)
    for (var i = 0; i < data.length; i++) {
        var optionButton = document.createElement("option");
        var pTag = document.createElement("p");
        var sample_id = data[i]
        optionButton.text = sample_id;
        optionButton.value = sample_id;
        document.getElementById("selDataset").appendChild(optionButton);
    }
    // var item = d3.select('#selDataset')
    // item.selectAll('option').data(data).enter().append('option').text(function(d){
    //     return d;
    // });
})

function makeChartjsFromCountryData(countryData){
    beanslist = []
    fruitlist = []
    juicelist = []
    milklist  = []
    veglist   = []
    nutlist   = []
    proteinlist = []
    redmeatlist = []
    sodalist = []
    // countryData.forEach(i=>
    for (var i = 0; i < foodYears.length; i++){
        // console.log(countryData[i])
       beanslist.push(countryData[foodYears[i]][0]["beans"]);
       fruitlist.push(countryData[foodYears[i]][0]["fruit"]);
       juicelist.push(countryData[foodYears[i]][0]["fruitJuice"]);
       milklist.push(countryData[foodYears[i]][0]["milk"]);
       veglist.push(countryData[foodYears[i]][0]["nsVeg"]);
       nutlist.push(countryData[foodYears[i]][0]["nuts"]);
       proteinlist.push(countryData[foodYears[i]][0]["protein"]);
       redmeatlist.push(countryData[foodYears[i]][0]["redMeat"]);
       sodalist.push(countryData[foodYears[i]][0]["soda"]);
    }
    
        return {
            labels: foodYears,
            datasets:[{
                label: 'Beans',
                borderColor: 'brown',
                data: beanslist
            },{
                label: 'Fruit',
                borderColor: 'yellow',
                data: fruitlist
            },{
                label: 'Fruit Juice',
                borderColor: 'orange',
                data: juicelist
            },{
                label: 'Milk',
                borderColor: 'black',
                data: milklist
            },{
                label: 'Non Starchy Vegetables',
                borderColor: 'green',
                data: veglist
            },{
                label: 'Nuts',
                borderColor: 'blue',
                data: nutlist
            },{
                label: 'Protein',
                borderColor: 'yellow',
                data: proteinlist
            },{
                label: 'Red Meat',
                borderColor: 'red',
                data: redmeatlist
            },{
                label: 'Soda-pop',
                borderColor: 'pink',
                data: sodalist
            }]
}
}

d3.json(baseURL + base_country_food_data + starting_country, function(data){
    console.log(data) //food data
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type:'line',
        data:makeChartjsFromCountryData(data),
        options: {
            title: {
                display: true,
                text: 'Food Comsumpion per year from USA, Puerto Rico and US Virgin Islands in Grams'
            }
        }
})


d3.selectAll("#selDataset").on("change", function(d){
    var dropdownMenu = d3.select("#selDataset");
    var dataset = dropdownMenu.property("value");
    console.log(dataset);
    chart.destroy()
    d3.json(baseURL+base_country_food_data+dataset, function(data){
        console.log(data)
        var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {
        type:'line',
        data: makeChartjsFromCountryData(data),
        options: {
            title: {
                display: true,
                text: `Food Comsumpion per year from ${dataset} in Grams`
            },
            scales: {
                yAxes: [{
                  scaleLabel: {
                    display: true,
                    labelString: 'probability'
                  }
                }]
              }     
            
            }
        }
    )
    })
})
})