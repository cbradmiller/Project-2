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
d3.json(baseURL + USHCURL, function(data){
    console.log(data) //healthcare data
})
//call the api for the food indexes to set up that dropdown menu

//call the other api to get the data for the other things, starting on us?