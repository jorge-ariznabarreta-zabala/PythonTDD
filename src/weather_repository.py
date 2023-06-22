WEATHER_DB = {
    "BIO": {"id": "BIO", "name": "Bilbao", "temperature": 30, "rain_probability": 0.1},
    "RMA": {"id": "RMA", "name": "Roma", "temperature": 22, "rain_probability": 0.2},
}


def create(weather):
    id = weather["id"]
    WEATHER_DB[id] = weather


def read(id):
    return WEATHER_DB.get(id)


def read_all():
    return WEATHER_DB


def delete(id):
    del WEATHER_DB[id]
