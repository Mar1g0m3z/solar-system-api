from app.db import db
from app.models.planets import Planet

# get all planet


def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    # act
    response = client.get("/planets")
    # assert
    assert response.status_code == 200
    assert response.get_json() == []

# return empty when db is empty


def test_get_one_planet_returns_seeded_planet(client, one_planet):
    # act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()
    # assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["number_of_moons"] == one_planet.number_of_moons

# get one planet returns seeded planet


def test_create_planet_path(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "Uranus",
        "description": "Don't even say it.",
        "number_of_moons": 3
    }
    # act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_json()
    # assert
    assert response.status_code == 201
    assert response_body["id"] == 1
    assert response_body["name"] == EXPECTED_PLANET["name"]
    assert response_body["description"] == EXPECTED_PLANET["description"]
    assert response_body["number_of_moons"] == EXPECTED_PLANET["number_of_moons"]

    # check if db is updated
    query = db.select(Planet).where(Planet.id == 1)
    new_planet = db.session.scalar(query)
    # we can compare these values with EXPECTED_CAT
    assert new_planet.id == 1
    assert new_planet.name == EXPECTED_PLANET["name"]
    assert new_planet.description == EXPECTED_PLANET["description"]
    assert new_planet.number_of_moons == EXPECTED_PLANET["number_of_moons"]

# test create planet
