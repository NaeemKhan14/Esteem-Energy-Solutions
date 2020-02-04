import flask
from flask import jsonify
from threading import Timer
from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
Devices = [
    { 
        "Lamp":
        [
            {
             'id': 1,
             'DeviceName': 'Lamp 1',
             'ElecConsp': '20 kWh'
            },
            {
             'id': 0,
             'DeviceName': 'Lamp 2',
             'ElecConsp': '1 kWh'
            }
        ]
    },
    
    {
        "Fridge":
        [
            {
             'id': 1,
             'DeviceName': 'Fridge 1',
             'ElecConsp': '500 kWh'
            },
            {
             'id': 0,
             'DeviceName': 'Fridge 2',
             'ElecConsp': '15 kWh'
             }
        ]
    },    

    {
        "Tv":
        [
            {
             'id': 1,
             'DeviceName': 'Tv 1',
             'ElecConsp': '90 kWh'
            },
            {
             'id': 0,
             'DeviceName': 'Tv 2',
             'ElecConsp': '2 kWh'
            }
        ]
    },

    {
        "AC":
        [
            {
             'id': 1,
             'DeviceName': 'Ac 1',
             'ElecConsp': '3000 kWH'
            },
            {
             'id': 0,
             'DeviceName': 'Ac 2',
             'ElecConsp': '20 kWh'
            }
        ]
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
@app.route('/api/v1/kawaii', methods=['GET'])
def api_all():
    return jsonify(Devices)

app.run()