from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

#just have to set up the engine. Like below.

# engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    return(
        "Available Routes:<br/>"
        "/api/v1.0/USHealthCare<br/>"
        "/api/v1.0/foodData/country_name<br/>"
        "/api/v1.0/countrynames<br/>"
        "/api/v1.0/dataFoodIndex<br/>"
    )

@app.route("/api/v1.0/USHealthCare")
def healthcareCost():
    #untested
    healthcareData = session.querry("select * from us_healthcare_costs_percapita;")
    return(jsonify(healthcareData))

@app.route("/api/v1.0/foodData/<countryName>")
def foodDataByCountry(countryName):
    #untested
    countryFood = {
        "1990": session.querry(f"select * from median_data_1990 where lower(countryname) = lower('{countryName}');"),
        "1995": session.querry(f"select * from median_data_1995 where lower(countryname) = lower('{countryName}');"),
        "2000": session.querry(f"select * from median_data_2000 where lower(countryname) = lower('{countryName}');"),
        "2005": session.querry(f"select * from median_data_2005 where lower(countryname) = lower('{countryName}');"),
        "2010": session.querry(f"select * from median_data_2010 where lower(countryname) = lower('{countryName}');"),
        "2015": session.querry(f"select * from median_data_2015 where lower(countryname) = lower('{countryName}');")
    }
    return(jsonify(countryFood))

@app.route("/api/v1.0/countrynames")
def getCountryNames():
    #untested
    namesOfCountries = {"countryNames": session.querry('select countryname from median_data_1990;')}
    return(jsonify(namesOfCountries))

@app.route("/api/v1.0/dataFoodIndex")
def getFoodIndex ():
    #this may have to do, unless there is an easy way to get the indexs of the db.
    indexNames = {"indexs":[fruit_consumption,
	nonstarchy_vegetable_consumption,
	beans_and_legumes,
	nuts_and_seeds,
	unprocessed_red_meat,
	sugarsweetened_beverages,
	fruit_juices,
	protein,
	calcium_milligrams,
	potassium_milligrams,
	total_milk]}
    return(jsonify(indexNames))


if __name__ == '__main__':
    app.run(debug = True)