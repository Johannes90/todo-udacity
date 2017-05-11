from models.base import Base
from models.base import db


class ProjectModel(Base):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    todos = db.relationship('TodoModel', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, name, user_id=None):
        self.name = name,
        self.user_id = user_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'todos': [todo.json() for todo in self.todos.all()]
            }
