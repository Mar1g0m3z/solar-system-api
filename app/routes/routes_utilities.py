from flask import abort, make_response
from ..db import db


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        invalid_response = {
            "message": f"{cls.__name__} id ({model_id}) is invalid."}
        abort(make_response(invalid_response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        not_found = {
            "message": f"{cls.__name__} with id ({model_id}) not found."}
        abort(make_response(not_found, 404))
    return model


def get_models_with_filters(cls, filters=None):
    query = db.select(cls)

    if filters:
        for attribute, value in filters.items():
            if hasattr(cls, attribute):
                attr = getattr(cls, attribute)
            if isinstance(value, str) and str(attr.type) in ["VARCHAR", "TEXT", "String"]:
                query = query.where(attr.ilike(f"%{value}%"))
            else:
                query = query.where(attr == value)
    models = db.session.scalars(query.order_by(cls.id))
    models_response = [model.to_dict() for model in models]
    # list comprehension
    # hecking weird naming list loop thingy

    return models_response


def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_model)
    db.session.commit()
    return new_model.to_dict(), 201
