import pytest
from src.webserver import create_app

@pytest.fixture
def client():
    app=create_app("weather_test.db")
    with app.test_client() as client:
        yield client

def test_get_root(client):
    result = client.get("/")
    assert result.text == 'Hola'
    assert result.status_code== 200
