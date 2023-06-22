import pytest
from src.webserver import create_app

app = create_app("weather.db")
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_root(client):
    result = client.get("/")
    assert result.text == 'Hola'
    assert result.status_code== 200
