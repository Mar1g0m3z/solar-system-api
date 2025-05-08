from flask import abort, Blueprint, make_response, request
from app.models.moons import Moon
from app.models.planets import Planet
from .routes_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")


@bp.post("")
def create_moon():
    request_body = request.get_json()

    return create_model(Moon, request_body)


@bp.post("/<id>/planets")
def create_moon_with_planet_id(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)


@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)


@bp.get("/<id>/planets")
def get_all_planet_moons(id):
    planet = validate_model(Planet, id)
    moons = [moon.to_dict() for moon in planet.moons]
    
    return moons
