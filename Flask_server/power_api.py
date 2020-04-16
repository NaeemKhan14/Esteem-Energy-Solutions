import flask
from flask import jsonify

power_app = flask.Flask(__name__)
power_app.config["DEBUG"] = True

PowerSources = [
    {
        'SourceName': 'Battery1',
        'type': 'Battery',
        'SupplyingPower': False,
        'ChargingState': False,
        'MaximumCapacity': 15.0,
        'RemainingCapacity': 15.0,
        'CurrentSupplied': 0,
        'BatteryPercentage': 100

    },

    {
        'SourceName': 'SolarPanel1',
        'type':'EnergyGenerator',
        'CurrentGenerated':3.68,
        'SupplyingPower': False,
        'ChargingState': False,
        'CurrentSupplied': 0

    },

    {
        'SourceName': 'PowerGrid1',
        'type':'Grid',
        'SupplyingPower': False,
        'PowerCut': True,
        'CurrentSupplied': 0

    }

]

Battery1 = next(item for item in PowerSources if item["SourceName"] == 'Battery1')

#Solar panel Simulator




@power_app.route('/api', methods=['GET'])
def all_sources():
    return jsonify(PowerSources)


@power_app.route('/api/batterydischarge/<float:discharge>', methods=['GET'])
def batteryTransaction(discharge):
    if Battery1['RemainingCapacity'] - discharge >= 0:
        Battery1['CurrentSupplied'] += discharge
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
        Battery1['CurrentSupplied'] = charge
        Battery1['RemainingCapacity'] += charge
        Battery1['ChargingState'] = True
        if Battery1['RemainingCapacity'] == Battery1['MaximumCapacity']:
            Battery1['ChargingState'] = False
    else:

        Battery1['ChargingState'] = False

    Battery1['BatteryPercentage'] = int(Battery1['RemainingCapacity'] / Battery1['MaximumCapacity'] * 100)
    return jsonify(PowerSources)


@power_app.route('/api/givepower/<string:source>/<float:charge>', methods=['GET'])
def powerSupply(source, charge):
    if source == 'Battery1':
        return jsonify("Error wrong method used for battery.")
    Source1 = next(item for item in PowerSources if item["SourceName"] == source)
    Source1['SupplyingPower'] = True
    Source1['CurrentSupplied'] += charge
    if charge == 0.0:
        Source1['SupplyingPower'] = False
    return jsonify(PowerSources)

if __name__ == '__main__':
    power_app.run(port=12345)
