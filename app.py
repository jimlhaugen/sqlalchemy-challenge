# Import the dependencies.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

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
# 1. Import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def Precipitation():
     """Convert the query results from your precipitation analysis (i.e., retrieve only the last 12 months of data) to a dictionary using <date> as the key and <prcp> as the value."""
     """Returns the JSON represenation of the dictionary"""
     dictionary = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= '2016-08-23')
     dictionary=[each_result[0] for each_result in dictionary]
     return jsonify(dictionary)


@app.route("/api/v1.0/stations")
def Stations():
    """Return a JSON list of stations the dataset."""

    active_stations=session.query(Measurement.station).limit(5).all()
    print(active_stations)
    active_stations=[each_result[0] for each_result in active_stations]
    return jsonify(active_stations)


@app.route("/api/v1.0/tobs")
def Tobs():
    """Returns a JSON list of temperature observations of the previous year"""
    tobs = session.query(Measurement.tobs).\
    filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()  # between is inclusive
    results=[each_result[0] for each_result in tobs]
    return jsonify(results)


@app.route("/api/v1.0/<start>")
def start_date():
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for the start date"""
    TMIN = session.query(func.min(Measurement.tobs)).\
            filter(Measurement.date == '2016-08-23')
    TAVG = session.query(func.avg(Measurement.tobs)).\
            filter(Measurement.date == '2016-08-23')
    TMAX = session.query(func.max(Measurement.tobs)).\
            filter(Measurement.date == '2016-08-23')
    min_avg_max = TMIN, TAVG, TMAX
    min_avg_max_list = list(np.ravel(min_avg_max))
    min_avg_max_return = {'TMIN':min_avg_max_list[0], 'TAVG':min_avg_max_list[1], 'TMAX':min_avg_max_list[2]}
    return jsonify(min_avg_max_return)


@app.route("/api/v1.0/<start>/<end>")
def start_to_end():
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature from the start date to the end date, inclusive"""
    TMIN = session.query(func.min(Measurement.tobs)).\
            filter(Measurement.date.between('2016-08-23', '2017-08-23'))
    TAVG = session.query(func.avg(Measurement.tobs)).\
            filter(Measurement.date.between('2016-08-23', '2017-08-23'))
    TMAX = session.query(func.max(Measurement.tobs)).\
            filter(Measurement.date.between('2016-08-23', '2017-08-23'))
    min_avg_max = TMIN, TAVG, TMAX
    min_avg_max_list = list(np.ravel(min_avg_max))
    min_avg_max_return = {'TMIN':min_avg_max_list[0], 'TAVG':min_avg_max_list[1], 'TMAX':min_avg_max_list[2]}
    return jsonify(min_avg_max_return)

if __name__ == "__main__":
    app.run(debug=True)
