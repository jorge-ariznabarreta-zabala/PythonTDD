import pytest
from src.webserver import create_app
import sqlite3

@pytest.fixture
def client():
    app=create_app("weather_test.db")
    with app.test_client() as client:
        yield client

def test_get_root(client):
    result = client.get("/")
    assert result.text == 'Hola'
    assert result.status_code== 200

def test_get_city(client):
    #preparar ARRANGE
    con = sqlite3.connect("weather_test.db")
    cur = con.cursor()
    cur.executescript(
        '''
        DROP TABLE IF EXISTS cities;
        CREATE TABLE IF NOT EXISTS cities(id, name, temperature, rain_probability);
        INSERT INTO cities (id, name, temperature, rain_probability) VALUES ("BIO", "Bilbao",34, 0.5 )
        
        '''
        )
    #hacer la petición ACT
    result=client.get("/cities/BIO")
    #comprobar la respuesta ASSERT
    assert result.status_code==200
    assert result.json=={
        "id": "BIO",
        "name": "Bilbao",
        "temperature": 34,
        "rain_probability": 0.5
    }