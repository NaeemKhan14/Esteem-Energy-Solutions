import flask
from flask import jsonify
from threading import Timer
from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

Devices = [
            {
             'DeviceName': 'Lamp1',
             'ElecConsp': 0.02,
             'CurConsp': 0.02,
             'status':'on'
            },
            {
             'DeviceName': 'Lamp2',
             'ElecConsp': 0.03,
             'CurConsp': 0.03,
             'status':'on'
            },
            {
             'DeviceName': 'Fridge1',
             'ElecConsp': 0.13,
             'CurConsp': 0.13,
             'status':'on'
            },
            {
             'DeviceName': 'Fridge2',
             'ElecConsp': 0.15,
             'CurConsp': 0.15,
             'status':'on'
             },
             {
             'DeviceName': 'Tv1',
             'ElecConsp': 0.07,
             'CurConsp': 0.07,
             'status':'on'
            },
            {
             'DeviceName': 'Tv2',
             'ElecConsp': 0.08,
             'CurConsp': 0.08,
             'status':'on'
            },
            {
             'DeviceName': 'Ac1',
             'ElecConsp': 0.98,
             'CurConsp': 1.20,
             'status':'on'
            }

]



# # Selects a random item's Status from the list and changes it depending on its state.
# def randomize_data(interval):
    # global kawaii
    # Timer(interval, randomize_data, [interval]).start()
    # index = randint(0, len(kawaii) - 1)
    # kawaii[index]['Status'] = 'On' if kawaii[index]['Status'] == 'Off' else 'Off'

# # Change status every second.
# randomize_data(1)

# A route to return all of the available entries in our catalog.
@app.route('/api/<string:device_id>', methods=['GET'])
def api_all(device_id):

    for device in range(len(Devices)):
        print(Devices[device]['DeviceName'])
        if Devices[device]['DeviceName'] == device_id:
            return jsonify(Devices[device])

    return jsonify('No device exsists with this id')


#Used to turn on and off any device 
@app.route('/api/changestatus/<string:device_id>', methods=['GET'])
def api_status(device_id):
    for device in range(len(Devices)):
        print(Devices[device]['DeviceName'])
        if Devices[device]['DeviceName'] == device_id:
            if Devices[device]['status'] == 'on':
               Devices[device]['status'] = 'off'
               Devices[device]['CurConsp'] = '0'

            else:
               Devices[device]['status'] = 'on'
               Devices[device]['CurConsp'] = Devices[device]['ElecConsp']
               
            return jsonify(Devices[device])

    return jsonify('No device exsists with this id') 

@app.route('/api/energyconsumption/<string:device_id>', methods=['GET'])
def device_consumption(device_id):
    for device in range(len(Devices)):
        print(Devices[device]['DeviceName'])
        if Devices[device]['DeviceName'] == device_id:
            return jsonify(Devices[device]['CurConsp'])

    return jsonify('No device exsists with this id')

@app.route('/api/alldevicesconsumption/', methods=['GET'])
def total_consumption():
    for device in Devices:
        return jsonify(Devices)

    return jsonify('No device exsists in the api')




app.run()
