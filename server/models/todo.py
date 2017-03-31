from db import db


class TodoModel(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(200))
    done = db.Column(db.Boolean())
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

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
        return {'id': self.id,
                'desc': self.desc,
                'done': self.done,
                'project': self.project.query.first().name,
                'created_by': self.user.query.first().username
               }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
