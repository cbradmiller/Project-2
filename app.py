
import numpy as np
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, DateTime
from dateutil.relativedelta import relativedelta
import datetime as dt

from flask import Flask, jsonify
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

Base = automap_base()
Base.prepare(engine, reflect=True)

data_1990 = Base.classes.median_data_1990
data_1995 = Base.classes.median_data_1995
data_2000 = Base.classes.median_data_2000
data_2005 = Base.classes.median_data_2005
data_2010 = Base.classes.median_data_2010


app = Flask(__name__)

@app.route("/")
def home_page():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/Healthcarecosts<br/>"
        # f"/api/v1.0/stations<br/>"
        # f"/api/v1.0/tobs<br/>"
        # f"/api/v1.0/<start><br/>"
        # f"/api/v1.0/<start>/<end><br/>"
    )
@app.route("/api/v1.0/Healthcarecosts")
def healthcare_data():
    session = Session(engine)
    all_m = session.query(data_1990.countryname,data_1990.fruit_consumption).all()
    session.close()
    all_measure = []
    for country, fruit in all_m:
        data_dict = {}
        data_dict["Date"] = country
        data_dict["Precipitation"] = fruit
        all_measure.append(data_dict)

    return jsonify(all_measure)


# @app.route("/api/v1.0/foodData/<countryName>")
# def foodDataByCountry(countryName):
#     #untested
#     countryFood = {
#         "1990": session.query(f"select * from median_data_1990 where lower(countryname) = lower('{countryName}');"),
#         "1995": session.query(f"select * from median_data_1995 where lower(countryname) = lower('{countryName}');"),
#         "2000": session.query(f"select * from median_data_2000 where lower(countryname) = lower('{countryName}');"),
#         "2005": session.query(f"select * from median_data_2005 where lower(countryname) = lower('{countryName}');"),
#         "2010": session.query(f"select * from median_data_2010 where lower(countryname) = lower('{countryName}');"),
#         "2015": session.query(f"select * from median_data_2015 where lower(countryname) = lower('{countryName}');")
#     }
#     return(jsonify(countryFood))

# @app.route("/api/v1.0/countrynames")
# def getCountryNames():
#     #untested
#     namesOfCountries = {"countryNames": session.query('select countryname from median_data_1990;')}
#     return(jsonify(namesOfCountries))

# @app.route("/api/v1.0/dataFoodIndex")
# def getFoodIndex ():
#     #this may have to do, unless there is an easy way to get the indexs of the db.
#     indexNames = {"indexs":[fruit_consumption,
# 	nonstarchy_vegetable_consumption,
# 	beans_and_legumes,
# 	nuts_and_seeds,
# 	unprocessed_red_meat,
# 	sugarsweetened_beverages,
# 	fruit_juices,
# 	protein,
# 	calcium_milligrams,
# 	potassium_milligrams,
# 	total_milk]}
#     return(jsonify(indexNames))