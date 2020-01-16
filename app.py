from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

# more stuff to put in here once we get our data set up. Like below.

# engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# Measurement = Base.classes.measurement
# Station = Base.classes.station

# session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    return(
        "Available Routes:<br/>"
        "/api/v1.0/USHealthCare<br/>"
        "api/v1.0/foodData/country_name<br/>"
    )

@app.route("/api/v1.0/USHealthCare")
def healthcareCost():
    return(
        "whatever the healthcare cost stuff will be."
    )

@app.route("api/v1.0/foodData/<countryName>")
def foodDataByCountry(countryName):
    return(
        "get the data from that country and return as a json thing."
    )

if __name__ == '__main__':
    app.run(debug = True)