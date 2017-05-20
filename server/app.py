# Importing Flask and Extensions

from flask import Flask
from flask_jwt import JWT

# Importing Resources
from resources.todo import Todos
from resources.todo import Todo
from resources.project import Projects
from resources.project import Project
from resources.user import UserRegister
from resources.user import Users
from resources.user import GoogleSignUp

from extensions import (
    migrate,
    cors,
    api,
    bcrypt
)

from models.base import db


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object('config')

    from security import authenticate, identity
    JWT(app, authenticate, identity)

    routes(app)

    extensions(app)
    db.init_app(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """

    migrate.init_app(app, db)
    cors.init_app(app)
    bcrypt.init_app(app)
    api.init_app(app)


def routes(app):
    """
    Register all api endpoints.

    :param app: Flask application instance
    :return: None
    """
    api.add_resource(Todos, '/todos')
    api.add_resource(Todo, '/todo/<int:id>')

    api.add_resource(Projects, '/projects')
    api.add_resource(Project, '/project/<int:id>')

    api.add_resource(GoogleSignUp, '/google-sign')
    api.add_resource(UserRegister, '/register')
    api.add_resource(Users, '/users')

