from flask import Blueprint
from app.models.planets import planets
# In Flask, url_prefix is an argument used when registering a blueprint. It adds a specified prefix to all routes defined within that blueprint.
# neat!
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():
    planet_response = []
    for planet in planets:
        # curiously  jason does not require key ordering, so things may be printed out of order
        planet_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "number of moons": planet.number_of_moons
            }
        )
    return planet_response
