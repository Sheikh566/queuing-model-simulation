from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from arrival_table import construct_avg_arrival_lookup_table
from simulation import construct_simulation_table
from queuing_formulae import calculate_averages_by_formula

app = Flask(__name__)
CORS(app)


@app.route("/get-interarrival-lookup-table", methods=["GET"])
@cross_origin()
def get_interarrival_lookup_table():
    print(request.args)
    arrival_dist_type = eval(request.args.get("arrivalDistType"))
    arrival_mean = eval(request.args.get("meanArrival"))
    arrival_variance = eval(request.args.get("varianceArrival"))
    arrival_table = construct_avg_arrival_lookup_table(
        arrival_dist_type, arrival_mean, arrival_variance
    )
    response = arrival_table.values.tolist()
    return jsonify(response), 200


@app.route("/get-complete-simulation", methods=["GET"])
@cross_origin()
def get_complete_simulation():
    print(request.args)
    num_of_servers = eval(request.args.get("numOfServers"))
    arrival_dist_type = eval(request.args.get("arrivalDistType"))
    arrival_mean = eval(request.args.get("meanArrival"))
    service_dist_type = eval(request.args.get("serviceDistType"))
    service_mean = eval(request.args.get("meanService"))
    arrival_variance = None
    service_variance = None
    try:
        arrival_variance = eval(request.args.get("varianceArrival"))
    except:
        pass
    try:
        service_variance = eval(request.args.get("varianceService"))
    except:
        pass

    arrival_table = construct_avg_arrival_lookup_table(
        arrival_dist_type, arrival_mean, arrival_variance
    )
    arrival_table = arrival_table.values.tolist()

    simulation_table, servers, averages = construct_simulation_table(
        num_of_servers,
        len(arrival_table),
        arrival_dist_type,
        arrival_mean,
        service_dist_type,
        service_mean,
        arrival_variance,
        service_variance,
    )

    response = {
        "simulationTable": simulation_table.values.tolist(),
        "servers": servers,
        "averages": averages,
        "cumulativeTable": arrival_table
    }
    return jsonify(response), 200


@app.route("/get-averages", methods=["GET"])
def get_averages():
    print(request.args)
    num_of_servers = eval(request.args.get("numOfServers"))
    arrival_dist_type = eval(request.args.get("arrivalDistType"))
    arrival_mean = eval(request.args.get("meanArrival"))
    service_dist_type = eval(request.args.get("serviceDistType"))
    service_mean = eval(request.args.get("meanService"))
    arrival_variance = eval(request.args.get("varianceArrival"))
    service_variance = eval(request.args.get("varianceService"))

    response = calculate_averages_by_formula(
        num_of_servers,
        arrival_dist_type,
        arrival_mean,
        service_dist_type,
        service_mean,
        arrival_variance,
        service_variance,
    )

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
