import flask
from flask import jsonify
from threading import Timer
from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
kawaii = [
    {'id': 0,
     'name': 'Smart Plug',
     'power_consumption': '10 Watts',
     'Status': 'Off'},
    {'id': 1,
     'name': 'Smart Light',
     'power_consumption': '20 Watts',
     'Status': 'On'},
    {'id': 2,
     'name': 'Air Conditioner',
     'power_consumption': '69 Watts',
     'Status': 'Off'}
]

# Selects a random item's Status from the list and changes it depending on its state.
def randomize_data(interval):
    global kawaii
    Timer(interval, randomize_data, [interval]).start()
    index = randint(0, len(kawaii) - 1)
    if kawaii[index]['Status'] == 'Off':
        kawaii[index]['Status'] = 'On'
    else:
        kawaii[index]['Status'] = 'Off'

# Change status every second.
randomize_data(1)

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/kawaii', methods=['GET'])
def api_all():
    return jsonify(kawaii)

app.run()