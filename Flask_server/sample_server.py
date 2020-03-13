import flask
from flask import jsonify
##from threading import Timer
##from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

Devices = [
            {
             'DeviceName': 'Lamp1',
             'DeviceModel': 'Amazing Lights',
             'ElecConsp': 0.02,
             'CurConsp': 0.02,
             'status':'on',
             'ip_address': '127.0.0.2'
            },
            {
             'DeviceName': 'Lamp2',
             'DeviceModel': 'Amazing Lights',
             'ElecConsp': 0.03,
             'CurConsp': 0.03,
             'status':'on',
             'ip_address': '127.0.0.3'
            },
            {
             'DeviceName': 'Fridge1',
             'DeviceModel': 'Amazing Cooling',
             'ElecConsp': 0.13,
             'CurConsp': 0.13,
             'status':'on',
             'ip_address': '127.0.0.4'
            },
            {
             'DeviceName': 'Fridge2',
             'DeviceModel': 'Amazing Cooling',
             'ElecConsp': 0.15,
             'CurConsp': 0.15,
             'status':'on',
             'ip_address': '127.0.0.5'
             },
             {
             'DeviceName': 'Tv1',
             'DeviceModel': 'Amazing Entertainment',
             'ElecConsp': 0.07,
             'CurConsp': 0.07,
             'status':'on',
             'ip_address': '127.0.0.6'
            },
            {
             'DeviceName': 'Tv2',
             'DeviceModel': 'Amazing Entertainment',
             'ElecConsp': 0.08,
             'CurConsp': 0.08,
             'status':'on',
             'ip_address': '127.0.0.7'
            },
            {
             'DeviceName': 'Ac1',
             'DeviceModel': 'Amazing Cooling',
             'ElecConsp': 0.98,
             'CurConsp': 1.20,
             'status':'on',
             'ip_address': '127.0.0.8'
            }

]

PowerSources = [
            {
             'SourceName': 'Battery1',
             'EnergyLevel': 98,
             'Charging':'true',
             'SupplyingPower': 'false',
            },
            {
             'SourceName': 'SolarPanel1',
             'EnergyLevel': 50,
             'Charging':'false',
             'SupplyingPower': 'false',
            }

]



###Used to turn on and off any device 
@app.route('/api/changestatus/<string:device_id>', methods=['GET'])
def api_status(device_id):
   for device in Devices:
       
       if Devices[device]['DeviceName'] == device_id:
           if Devices[device]['status'] == 'on':
              Devices[device]['status'] = 'off'
              Devices[device]['CurConsp'] = 0

           else:
              Devices[device]['status'] = 'on'
              Devices[device]['CurConsp'] = Devices[device]['ElecConsp']
              
           return jsonify(Devices[device])

   return jsonify('No device exsists with this id') 
##

@app.route('/api/alldevicesconsumption/', methods=['GET'])
def total_consumption():
    return jsonify(Devices)

app.run()
