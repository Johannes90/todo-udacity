from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS, cross_origin

from security import authenticate, identity
from resources.todo import Todos
from resources.todo import Todo
from resources.project import Projects
from resources.project import Project
from resources.user import UserRegister
from resources.user import Users



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dev:dev@db:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisextremelysafe'

api = Api(app)



@app.before_first_request
def create_tables():
    """
    Create all tables before first request to API server is run.
    """
    db.create_all()
    print("Tables created")

jwt = JWT(app, authenticate, identity)

api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/todo/<int:id>')

api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<int:id>')

api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
