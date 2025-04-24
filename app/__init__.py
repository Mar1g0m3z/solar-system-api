from flask import Flask
from .db import db, migrate
from .models import planets
from .routes.planet_routes import planets_bp


def create_app():
    app = Flask(__name__)
<<<<<<< HEAD
=======

>>>>>>> 2e7592291e9da9c0b95b08b6bc3267deecef7729
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)

    return app
