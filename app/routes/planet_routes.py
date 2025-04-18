from flask import Blueprint
from app.models.planets import planets
# In Flask, url_prefix is an argument used when registering a blueprint. It adds a specified prefix to all routes defined within that blueprint.
# neat!
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    planet_response = []
    for planet in planets:
        # curiously  json does not require key ordering, so things may be printed out of order
        # it remembers insertion order, but it is not true for all dictionaries. FLASK ALPHABat? I cant spell guys , help
        # remember dictionaries are out of order
        planet_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "number_of_moons": planet.number_of_moons
                # dont put spaces in key names, json is  a weirdo, treat it like a valid vairable name.
            }
        )
    return planet_response


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    # handle wrong parameter in url. like a string and not a number that can be explicitly changed with int()
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"invalid planet {planet_id} invalid"}, 400
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {"id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "number_of_moons": planet.number_of_moons}
    return {"message": f"planet {planet_id} not found"}, 404

# Hey Tamika! Next steps i think its so make a helper function for the exception handeling helper to make code neater and make refractoring! If you read this comment let me know your thoughts or suggestions!
