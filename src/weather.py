from .weather_repository_sqlite import *


def add_city(weather):
    # weather = {"id": "MAD", "name": "Madrid", "temperature": 37}
    create(weather)


def get_weather_by(id):
    return read(id)


def list_weather_all():
    return read_all()


def delete_weather_by(id):
    delete(id)
