from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creates an instance of the database (Computer)
db = SQLAlchemy()

# Method of the application
def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from . import routes

        # Creates tables into our database using IDE
        db.create_all()

        return app