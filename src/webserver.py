from flask import Flask, request
from flask_cors import CORS
from .weather import *
def create_app(database):
    app = Flask(__name__)
    cors = CORS(app)

    init_db("weather.db")

    @app.route("/cities/<city_id>", methods=["GET"])
    def get_city(city_id):
        return get_weather_by(city_id)


    @app.route("/cities/<city_id>", methods=["DELETE"])
    def delete_city(city_id):
        print("DELETE")
        delete_weather_by(city_id)
        return ""


    @app.route("/cities/", methods=["GET"])
    def all_cities():
        return read_all()


    @app.route("/cities", methods=["POST"])
    def new_city():
        print("****new_city")
        # ¿Quien eres?
        user = request.headers['User']
        password = request.headers['Pass']

        if (not (user == "admin" and password == "admin")):
            return 'Usuaria no autorizada.', 403

        data = request.get_json()
        add_city(data)
        return ""


    @app.route("/", methods=["GET"])
    def hello_world():
        return "Hola"
    return app