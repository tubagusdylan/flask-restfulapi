from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_by_name
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV")
    app.config.from_object(config_by_name[env])
    db.init_app(app)

    # ini untuk meregister route agar terbaca setelah inisialisasi db
    from app.routes import register_routes
    register_routes(app)

    return app;