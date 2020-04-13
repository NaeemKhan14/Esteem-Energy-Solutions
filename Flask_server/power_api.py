import flask
from flask import jsonify

power_app = flask.Flask(__name__)
power_app.config["DEBUG"] = True

PowerSources = [
    {
        'SourceName': 'Battery1',
        'SupplyingPower': False,
        'ChargingState': False,
        'MaximumCapacity': 15.0,
        'RemainingCapacity': 15.0,
        'CurrentSupplying': 0,
        'BatteryPercentage': 100

    },

    {
        'SourceName': 'SolarPanel1',
        'SupplyingPower': False,
        'ChargingState': False,
        'CurrentSupplying': 0

    },

    {
        'SourceName': 'PowerGrid1',
        'SupplyingPower': False,
        'PowerCut': False,
        'CurrentSupplying': 0

    }

]

Battery1 = next(item for item in PowerSources if item["SourceName"] == 'Battery1')


@power_app.route('/api', methods=['GET'])
def all_sources():
    return jsonify(PowerSources)


@power_app.route('/api/batterydischarge/<float:discharge>', methods=['GET'])
def batteryTransaction(discharge):
    if Battery1['RemainingCapacity'] - discharge >= 0:
        Battery1['CurrentSupplying'] += discharge
        Battery1['RemainingCapacity'] -= discharge
        Battery1['SupplyingPower'] = True
        if Battery1['RemainingCapacity'] == 0:
            Battery1['SupplyingPower'] = False
    else:
        Battery1['SupplyingPower'] = False
    Battery1['BatteryPercentage'] = int(Battery1['RemainingCapacity'] / Battery1['MaximumCapacity'] * 100)
    return jsonify(PowerSources)


@power_app.route('/api/batterycharge/<float:charge>', methods=['GET'])
def batteryCharging(charge):
    if Battery1['RemainingCapacity'] + charge <= Battery1['MaximumCapacity']:
        Battery1['CurrentSupplying'] = charge
        Battery1['RemainingCapacity'] += charge
        Battery1['ChargingState'] = True
        if Battery1['RemainingCapacity'] == Battery1['MaximumCapacity']:
            Battery1['ChargingState'] = False
    else:

        Battery1['ChargingState'] = False

    Battery1['BatteryPercentage'] = int(Battery1['RemainingCapacity'] / Battery1['MaximumCapacity'] * 100)
    return jsonify(PowerSources)


power_app.run(port=12345)
