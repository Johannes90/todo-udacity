from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from models.todo import TodoModel
from models.project import ProjectModel
from models.user import UserModel


class Todo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('desc',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        ),
    parser.add_argument('done',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, id):
        todo = TodoModel.find_by_id(id)
        if todo:
            return todo.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def delete(self, id):
        print(current_identity)
        todo = TodoModel.find_by_id(id)
        # Implement Check to get current user = todo.creator
        if todo:
            if current_identity.username == todo.created_by:
                todo.delete_from_db()
            else:
                return {'message': 'Sorry, this todo was not created by you.'}
            return {'message': 'Todo deleted'}

    @jwt_required()
    def put(self, id):
        data = Todo.parser.parse_args()

        todo = TodoModel.find_by_id(id)

        if TodoModel.find_by_id(id):
            todo.desc = data['desc']
            todo.done = data['done']
            todo.save_to_db()
            return todo.json()
        else:
            return {'message': 'Todo not found'}, 404


class Todos(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('desc',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        ),
    parser.add_argument('project_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        ),
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self):
        return {'todos': list(map(lambda x: x.json(), TodoModel.query.all()))}

    def post(self):
        data = Todos.parser.parse_args()
        todo = TodoModel(desc=data['desc'], done='false',
                         project_id=data['project_id'], user_id=data['user_id'])

        if(ProjectModel.find_by_id(todo.project_id)):
            if(UserModel.find_by_id(todo.user_id)):
                try:
                    todo.save_to_db()
                    return todo.json(), 201
                except:
                    return {"message": "An error occurred inserting the todo."}, 500
            else:
                return {"message": "The associated user does not exist."}, 500
        else:
            return {"message": "The associated project does not exist."}, 500
