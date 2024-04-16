# Import the dependencies.
# Copy and paste from climate_starter.ipynb file

from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# reflect the tables
Base.prepare(autoload_with = engine, reflect = True)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def Precipitation():
    """Convert the query results from your precipitation analysis (i.e., retrieve only the last 12 months of data) to a dictionary using <date> as the key and <prcp> as the value."""
    """Returns the JSON represenation of the dictionary"""
    return jsonify(dictionary)

@app.route("/api/v1.0/stations")
def Stations():
    """Return a JSON list of stations the dataset."""
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def justice_league():
    """Returns a JSON list of temperature observations of the previous year"""

    return jsonify(justice_league_members)@app.route("/api/v1.0/justice-league")

@app.route("/api/v1.0/<start>")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)

@app.route("/api/v1.0/<end>")
def justice_league():
    """Return the justice league data as json"""
