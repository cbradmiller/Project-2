from flask import Flask, jsonify
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

Base = automap_base()
Base.prepare(engine, reflect=True)

median_data_1990 = Base.classes.median_data_1990
median_data_1995 = Base.classes.median_data_1995
median_data_2000 = Base.classes.median_data_2000
median_data_2005 = Base.classes.median_data_2005
median_data_2010 = Base.classes.median_data_2010

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
    healthcareData = session.query("select * from us_healthcare_costs_percapita;")
    return(jsonify(healthcareData))

@app.route("/api/v1.0/foodData/<countryName>")
def foodDataByCountry(countryName):
    #untested
    countryFood = {
        "1990": session.query(f"select * from median_data_1990 where lower(countryname) = lower('{countryName}');"),
        "1995": session.query(f"select * from median_data_1995 where lower(countryname) = lower('{countryName}');"),
        "2000": session.query(f"select * from median_data_2000 where lower(countryname) = lower('{countryName}');"),
        "2005": session.query(f"select * from median_data_2005 where lower(countryname) = lower('{countryName}');"),
        "2010": session.query(f"select * from median_data_2010 where lower(countryname) = lower('{countryName}');"),
        "2015": session.query(f"select * from median_data_2015 where lower(countryname) = lower('{countryName}');")
    }
    return(jsonify(countryFood))

@app.route("/api/v1.0/countrynames")
def getCountryNames():
    #untested
    namesOfCountries = {"countryNames": session.query('select countryname from median_data_1990;')}
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