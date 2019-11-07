import pymysql

pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from CloudWebsiteAssignment3.config import Config
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from CloudWebsiteAssignment3.models.users import load_user
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from CloudWebsiteAssignment3.endpoints.Index.routes import main
    from CloudWebsiteAssignment3.endpoints.Login.routes import login

    app.register_blueprint(main)
    app.register_blueprint(login)
    return app
