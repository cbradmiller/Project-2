var foodYears = [1990, 1995, 2000, 2005, 2010, 2015];
//maybe I should get these dynamically, but here they are without that.
var healthYears = [1991,1992,1993,1994,1995,1996,1997,
    1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,
    2008,2009,2010,2011,2012,2013,2014]

var baseURL = 'https://learning-heroku-ido.herokuapp.com'
var USHCURL = '/api/v1.0/USHealthCare'
var cnameURL = '/api/v1.0/countrynames'
var foodIURL = '/api/v1.0/dataFoodIndex'
var base_country_food_data = '/api/v1.0/foodData/' //and then the country name
var starting_country =  "USA, Puerto Rico and US Virgin Islands"
var samples;
var year;
var money;
d3.json(baseURL + USHCURL, function(data){
    samples = data;
    year = [];
    money = [];
    var length = samples.length;
    console.log(length)
    
    for (var x = 0; x < length; x++) {
        
        money.push(samples[x]['per_cap_cost'])
        year.push(data[x]['year_cost'])
        
    }
    console.log(money)
        
    
var ctx = document.getElementById('myChart').getContext('2d');
            var chart = new Chart(ctx, {
             // The type of chart we want to create
            type: 'line', //also works as 'line, and then bacgroundColor may not be needed.'
    // The data for our dataset
            data: {
                labels: year,
                datasets: [{
                    label: 'US Per Capita Heathcare cost!',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: money
                }]
            },
    // Configuration options go here
    options: {}
});
});

d3.json(baseURL + base_country_food_data + starting_country, function(data){
    console.log(data) //food data
    sodalist = []
    // countryData.forEach(i=>
    for (var i = 0; i < foodYears.length; i++){
        // console.log(countryData[i])
       sodalist.push(data[foodYears[i]][0]["soda"]);
    }
    console.log(sodalist)
    var ctx = document.getElementById('popChart').getContext('2d');
    var chart = new Chart(ctx, {
        type:'line',
        data:{
            labels:foodYears,
            datasets:[{
                label:'US Sugary Drink(soda) Consumption.',
                backgroundColor: 'brown',
                borderColor: 'brown',
                data: sodalist

        }]},
        options: {
            title: {
                display: true,
                text: 'Soda per year from USA'
            }
        }
})});