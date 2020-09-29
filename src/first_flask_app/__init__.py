__version__ = "0.1.0"

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from .main import bp as bp_main
        app.register_blueprint(bp_main)

        return app
