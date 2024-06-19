from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .core import core as core_blueprint
    app.register_blueprint(core_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
