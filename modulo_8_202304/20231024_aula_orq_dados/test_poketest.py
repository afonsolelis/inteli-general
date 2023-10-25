import pytest
import app

@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    client = app.app.test_client()
    return client

def test_get_pokemon(client):
    response = client.get("/pokemon/pikachu")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["name"] == "pikachu"

def test_get_pokemon_not_found(client):
    response = client.get("/pokemon/nonexistentpokemon")
    assert response.status_code == 404
    json_data = response.get_json()
    assert "error" in json_data
