from flask import Flask
from flask_restful import Api
from resources.todo import Todos
from resources.todo import Todo
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisextremelysafe'

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/todo/<int:id>')


@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
