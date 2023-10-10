from flask import Flask, render_template, request
from marshmallow import Schema, fields
from utils.utils import (
    config_db,
    get_data_table,
    save_data,
    delete_data,
    update_data,
)


config_db()
app = Flask(__name__)


@app.route("/sensorsApi", methods=["GET", "POST"])
def sensorsApi():
    if request.method == "POST":
        # get data to the request body
        data = request.get_json()
        print(data)
        data_return = {}
        sensorPIR = None
        sensorDistance = None
        sensorTemperature = None
        try:
            # get the value of the 'sensorPIR' element
            sensorPIR = data["sensorPIR"]
            # get the value of the 'sensorDistance' element
            sensorDistance = data["sensorDistance"]
            # get the value of the 'sensorTemperature' element
            sensorTemperature = data["sensorTemperature"]
            # get the value of the 'sensorHumedad' element
            sensorHumedad = data["sensorHumedad"]
        except:
            pass
        # save the data in a variable
        if "sensorPIR" in data:
            data_return["sensorPIR"] = sensorPIR
        if "sensorDistance" in data:
            data_return["sensorDistance"] = sensorDistance
        if "sensorTemperature" in data:
            data_return["sensorTemperature"] = sensorTemperature
        if "sensorHumedad" in data:
            data_return["sensorHumedad"] = sensorHumedad
        print(data_return)
        save_data(data_return)
        return "POST OK"
    else:
        #  get the data from the database
        data_pir = get_data_table("SensorPir")
        data_distance = get_data_table("SensorDistance")
        data_temperature = get_data_table("SensorTemperature")
        data_humedad = get_data_table("SensorHumedad")
        # save the data in a variable
        data_return = {}
        data_return["sensorPIR"] = data_pir
        data_return["sensorDistance"] = data_distance
        data_return["sensorTemperature"] = data_temperature
        data_return["sensorHumedad"] = data_humedad
        print(data_return)
        return data_return


@app.route("/")
def home():
    # call the home.html file
    return render_template("home.html")
