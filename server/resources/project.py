from models.project import ProjectModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from models.user import UserModel

class Project(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )

    def get(self, id):
        project = ProjectModel.find_by_id(id)
        if project:
            return project.json()
        return {'message': 'Project not found'}, 404

    @jwt_required()
    def delete(self, id):
        project = ProjectModel.find_by_id(id)
        if project:
            if current_identity.id == project.user_id:
                project.delete_from_db()
                return {'message': 'Project deleted'}
            else:
                return {'message': 'Sorry, this project was not created by you.'}
        else:
                return {'message': 'Sorry, this project was not found.'}

    @jwt_required()
    def put(self, id):
        data = Project.parser.parse_args()
        project = ProjectModel.find_by_id(id)

        if project:
            if current_identity.id == project.user_id:
                project.name = data['name']
                project.save_to_db()
                return project.json()
            else:
                return {'message': 'Sorry, this project was not created by you.'}
        else:
            return {'message': 'Project not found'}, 404


class Projects(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        ),
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self):
        return {
            'projects': list(map(lambda x: x.json(), ProjectModel.query.all()))
            }

    @jwt_required()
    def post(self):
        data = Projects.parser.parse_args()
        project = ProjectModel(name=data['name'], user_id=data['user_id'])

        if(UserModel.find_by_id(project.user_id)):
            try:
                project.save_to_db()
                return project.json(), 201
            except:
                return {
                    "message": "An error occurred inserting the project."
                    }, 500
        else:
                return {"message": "The associated user does not exist."}, 500
