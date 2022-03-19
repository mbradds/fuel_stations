from flask import Flask, session
from flask_session import Session
import json
from flask_cors import CORS, cross_origin
from waitress import serve
import psutil
import os
import sys
from util import set_cwd_to_script
from vehicle_network import VehicleNetwork

set_cwd_to_script()
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
CORS(app,
     origins=["http://localhost:8080"],
     expose_headers=['Access-Control-Allow-Origin'],
     supports_credentials=True)
app.secret_key = 'supersecretkey'

app.config.update(SESSION_COOKIE_HTTPONLY=False,
                  SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
sess.init_app(app)
# app.config.update(
#     SECRET_KEY="secret_sauce",
#     SESSION_COOKIE_HTTPONLY=True,
#     REMEMBER_COOKIE_HTTPONLY=True,
#     SESSION_COOKIE_SAMESITE="Lax",
# )

process = psutil.Process(os.getpid())


# @app.after_request
# @cross_origin(origins="*", supports_credentials=True)
# def add_header(response):
#     response.headers.add('Access-Control-Allow-Headers',
#                          "Origin, X-Requested-With, Content-Type, Accept, x-auth")
#     return response


@app.route("/api/setInitialRoute", methods=["GET"])
def set_initial_route():
    if not "initpath" in session:
        session["initpath"] = VehicleNetwork(
            vehicle_fuel="ELEC", region="CA", vehicle_range=300)
        print("session path set", file=sys.stdout)
    else:
        session["initpath"] = session.get("initpath")
    return 'ok'


@app.route("/api/getRoute/<start_city>/<end_city>")
def get_route(start_city, end_city):
    return session.get("initpath").shortest_path(start_city, end_city)


@app.route("/api/updateNetwork/<f_type>/<vehicle_range>/<region>", methods=["PUT"])
def update_network(f_type, vehicle_range, region):
    session["initpath"] = VehicleNetwork(
        vehicle_fuel=f_type,
        region=region,
        vehicle_range=int(vehicle_range)
    )
    return {"new_fuel": f_type, "new_range": vehicle_range, "new_region": region}


@app.route("/api/getCityOptions", methods=["GET"])
def get_city_options():
    if "initpath" in session:
        return session.get("initpath").available_cities()
    else:
        return json.dumps(["City1", "City2"])


@app.route("/api/getVehicleRange")
def get_vehicle_range():
    return session.get("initpath").vehicle_range


@app.route("/api/memory")
def get_memory():
    return {'memory': process.memory_info().rss}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # serve(app, host="0.0.0.0", port=5000)
