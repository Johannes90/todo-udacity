# Importing Flask and Extensions

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt

# Importing JWT functions
from security import authenticate, identity

# Importing Resources
from resources.todo import Todos
from resources.todo import Todo
from resources.project import Projects
from resources.project import Project
from resources.user import UserRegister
from resources.user import Users
from resources.user import GoogleSignUp

# Creating the Flask Instance
app = Flask(__name__)
app.config.from_object('config')

# Wrapping the App instance with the CORS module to allow for cross server access
CORS(app)

# Wrapping the app instance with the Flask-Restful extension to enable API features
api = Api(app)

# Adding the flask-bcrypt extension

bcrypt = Bcrypt(app)

# Create database tables before first request (could be improved with migrations)
@app.before_first_request
def create_tables():
    """
    Create all tables before first request to API server is run.
    """
    db.create_all()
    print("Tables created")

jwt = JWT(app, authenticate, identity)

# Mapping the resources to endpoints with Flask Restful
api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/todo/<int:id>')

api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<int:id>')

api.add_resource(GoogleSignUp, '/google-sign')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')


# Launching the app
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
