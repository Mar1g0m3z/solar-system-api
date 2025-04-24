from flask import Blueprint, abort, make_response, request
from app.models.planets import Planet
from ..db import db
# In Flask, url_prefix is an argument used when registering a blueprint. It adds a specified prefix to all routes defined within that blueprint.
# neat!
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "number_of_moons": planet.number_of_moons,
                "description": planet.description
            }
        )

    return planets_response


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    number_of_moons = request_body["number_of_moons"]
    description = request_body["description"]

    new_planet = Planet(
        name=name, number_of_moons=number_of_moons, description=description)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "number_of_moons": new_planet.number_of_moons,
        "description": new_planet.description
    }

    return response, 201


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {{"message": f"invalid planet {planet_id} invalid"}}
#         abort(make_response(response, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))


# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     # handle wrong parameter in url. like a string and not a number that can be explicitly changed with int()
#     planet = validate_planet(planet_id)
#     return {"id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "number_of_moons": planet.number_of_moons}


# Hey Tamika! Next steps i think its so make a helper function for the exception handeling helper to make code neater and make refractoring! If you read this comment let me know your thoughts or suggestions!
