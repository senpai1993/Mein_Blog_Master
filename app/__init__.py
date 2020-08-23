from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    migrate.init_app(app, db)

    from app.error import bp as error_bp
    app.register_blueprint(error_bp)

    from app.category import bp as category_bp
    app.register_blueprint(category_bp)

    return app


from app import models
