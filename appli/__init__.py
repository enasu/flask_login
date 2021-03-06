from flask import Flask
from flask_login import LoginManager

from appli.database import initialize_database
from appli.models import User
from appli.views.auth import auth as auth_blueprint
from appli.views.main import main as main_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('appli.config.Config')
    initialize_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return User.query.get(str(email))

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app


app = create_app()
