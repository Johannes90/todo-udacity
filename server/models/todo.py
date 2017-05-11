from models.base import Base
from models.base import db


class TodoModel(Base):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(200))
    done = db.Column(db.Boolean())

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('ProjectModel')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, desc, done, project_id=None, user_id=None):
        self.desc = desc
        self.done = done
        self.project_id = project_id
        self.user_id = user_id

    def json(self):
        return {
                'id': self.id,
                'desc': self.desc,
                'done': self.done,
                'project': self.project.query.filter_by(id=self.project_id).first().name,
                'created_by': self.user.query.filter_by(id=self.user_id).first().username
               }
