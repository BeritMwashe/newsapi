
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap=Bootstrap()
def create_app(config_name):
    app=Flask(__name__)

    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)


    # regester bp
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)
    return app
# app.config.from_pyfile('config.py')
# bootstrap=Bootstrap(app)
# from app import views