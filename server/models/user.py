from models.base import Base
from models.base import db
from flask_bcrypt import generate_password_hash


class UserModel(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    oauth = db.Column(db.Boolean())

    todos = db.relationship('TodoModel', lazy='dynamic')
    projects = db.relationship('ProjectModel', lazy='dynamic')

    def __init__(self, username, password=None, oauth=False):
        self.username = username
        if password:
            self.password = generate_password_hash(password).decode('utf-8')
        else:
            self.password = password
        self.oauth = oauth

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'todos': [todo.json() for todo in self.todos.all()]
        }
