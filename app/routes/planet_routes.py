from flask import Blueprint, abort, make_response, request, Response
from .routes_utilities import validate_model, create_model,  get_models_with_filters
from app.models.planets import Planet
from ..db import db
# In Flask, url_prefix is an argument used when registering a blueprint. It adds a specified prefix to all routes defined within that blueprint.
# neat!
bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)


@bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()


@bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body)


@bp.put("/<id>")
def update_planet(id):
    planet = validate_model(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.number_of_moons = request_body["number_of_moons"]
    planet.description = request_body["description"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")


@bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)
    db.session.delete(planet)
    db.session.commit()
    return Response(status=204, mimetype="application/json")


# def validate_planet(id):
#     try:
#         id = int(id)
#     except ValueError:
#         invalid_response = {"message": f"Planet id({id})is invalid."}
#         abort(make_response(invalid_response, 400))

#     query = db.select(Planet).where(Planet.id == id)
#     planet = db.session.scalar(query)

#     if not planet:
#         not_found = {"message": f"Planet with id({id}) not found."}
#         abort(make_response(not_found, 404))

#     return planet
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
