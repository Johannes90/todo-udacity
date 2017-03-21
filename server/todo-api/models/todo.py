from db import db


class TodoModel(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(200))
    done = db.Column(db.Boolean())

    def __init__(self, desc, done):
        self.desc = desc
        self.done = done

    def json(self):
        return {'id': self.id, 'desc': self.desc, 'done': self.done}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
