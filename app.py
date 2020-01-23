from flask import Flask, jsonify
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

#just have to set up the engine. Like below.

# engine = create_engine("sqlite:///Resources/hawaii.sqlite")

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

Base = automap_base()
Base.prepare(engine, reflect=True)

# Measurement = Base.classes.measurement
# Station = Base.classes.station

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
    #working
    healthcareData = engine.execute("select * from us_healthcare_costs_percapita;")
    returnData = []
    for row in healthcareData:
        returnData.append({'year_cost': row[0], 'per_cap_cost': row[1]})

    return(jsonify(list(returnData)))

@app.route("/api/v1.0/foodData/<countryName>")
def foodDataByCountry(countryName):
    #untested
    data1990 = engine.execute(f"select * from median_data_1990 where lower(countryname) = lower('{countryName}');")
    mydata1990 = []
    for row in data1990:
        mydata1990.append({'countryName': row[0], 'fruit': row[1], 'nsVeg': row[2], 'beans':row[3], 'nuts':row[4], 'redMeat':row[5], 'soda':row[6], 'fruitJuice': row[7], 'protein': row[8],'milk':row[11]})

    data1995 = engine.execute(f"select * from median_data_1995 where lower(countryname) = lower('{countryName}');")
    mydata1995 = []
    for row in data1995:
        mydata1995.append({'countryName': row[0], 'fruit': row[1], 'nsVeg': row[2], 'beans':row[3], 'nuts':row[4], 'redMeat':row[5], 'soda':row[6], 'fruitJuice': row[7], 'protein': row[8],'milk':row[11]})

    data2000 = engine.execute(f"select * from median_data_2000 where lower(countryname) = lower('{countryName}');")
    mydata2000 = []
    for row in data2000:
        mydata2000.append({'countryName': row[0], 'fruit': row[1], 'nsVeg': row[2], 'beans':row[3], 'nuts':row[4], 'redMeat':row[5], 'soda':row[6], 'fruitJuice': row[7], 'protein': row[8],'milk':row[11]})

    data2005 = engine.execute(f"select * from median_data_2005 where lower(countryname) = lower('{countryName}');")
    mydata2005 = []
    for row in data2005:
        mydata2005.append({'countryName': row[0], 'fruit': row[1], 'nsVeg': row[2], 'beans':row[3], 'nuts':row[4], 'redMeat':row[5], 'soda':row[6], 'fruitJuice': row[7], 'protein': row[8],'milk':row[11]})

    data2010 = engine.execute(f"select * from median_data_2010 where lower(countryname) = lower('{countryName}');")
    mydata2010 = []
    for row in data2010:
        mydata2010.append({'countryName': row[0], 'fruit': row[1], 'nsVeg': row[2], 'beans':row[3], 'nuts':row[4], 'redMeat':row[5], 'soda':row[6], 'fruitJuice': row[7], 'protein': row[8],'milk':row[11]})

    data2015 = engine.execute(f"select * from median_data_2015 where lower(countryname) = lower('{countryName}');")
    mydata2015 = []
    for row in data2015:
        mydata2015.append({'countryName': row[0], 'fruit': row[1], 'nsVeg': row[2], 'beans':row[3], 'nuts':row[4], 'redMeat':row[5], 'soda':row[6], 'fruitJuice': row[7], 'protein': row[8],'milk':row[11]})

    countryFood = {
        "1990": mydata1990,
        "1995": mydata1995,
        "2000": mydata2000,
        "2005": mydata2005,
        "2010": mydata2010,
        "2015": mydata2015
    }
    return(jsonify(countryFood))

@app.route("/api/v1.0/countrynames")
def getCountryNames():
    #untested
    namesOfCountries = engine.execute('select countryname from median_data_1990;')
    dataToReturn = []
    for row in namesOfCountries:
        dataToReturn.append(row[0])
    return(jsonify(list(dataToReturn)))

@app.route("/api/v1.0/dataFoodIndex")
def getFoodIndex ():
    #this may have to do, unless there is an easy way to get the indexs of the db.
    indexNames = ['fruit_consumption',
	'nonstarchy_vegetable_consumption',
	'beans_and_legumes',
	'nuts_and_seeds',
	'unprocessed_red_meat',
	'sugarsweetened_beverages',
	'fruit_juices',
	'protein',
	'total_milk']
    return(jsonify(indexNames))


if __name__ == '__main__':
    app.run(debug = True)