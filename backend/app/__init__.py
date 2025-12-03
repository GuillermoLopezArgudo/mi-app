from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db
from .routes.main import main_bp
from .routes.auth import auth_bp

# Crear la aplicacion Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    # Inicializar DB
    db.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(main_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")

    return app
