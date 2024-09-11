from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import user_routes
from .swagger import configure_swagger
from src.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    CORS(app)  # Enable CORS for the entire application
    configure_swagger(app)  # Set up Swagger documentation

    # Register blueprints
    app.register_blueprint(user_routes.bp)

    return app
