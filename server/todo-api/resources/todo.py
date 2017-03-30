from models.todo import TodoModel
from models.project import ProjectModel
from flask_restful import Resource, reqparse

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

    def delete(self, id):
        todo = TodoModel.find_by_id(id)
        if todo:
            todo.delete_from_db()

        return {'message': 'Todo deleted'}

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
                    )

    def get(self):
        return {'todos': list(map(lambda x: x.json(), TodoModel.query.all()))}

    def post(self):
        data = Todos.parser.parse_args()
        print(data)
        todo = TodoModel(data['desc'], 'false', data['project_id'])

        try:
            todo.save_to_db()
        except:
            return {"message": "An error occurred inserting the todo."}, 500

        return todo.json(), 201
