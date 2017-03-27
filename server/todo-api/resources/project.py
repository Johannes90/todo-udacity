from models.project import ProjectModel
from flask_restful import Resource, reqparse

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

    def delete(self, id):
        project = ProjectModel.find_by_id(id)
        if project:
            project.delete_from_db()

        return {'message': 'Project deleted'}

    def put(self, id):
        data = Project.parser.parse_args()

        project = ProjectModel.find_by_id(id)

        if ProjectModel.find_by_id(id):
            project.name = data['name'] 
            project.save_to_db()
            return project.json()
        else:
            return {'message': 'Project not found'}, 404



class Projects(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self):
        return {'projects': list(map(lambda x: x.json(), ProjectModel.query.all()))}

    def post(self):
        data = Projects.parser.parse_args()

        project = ProjectModel(data['name'])
      
        # try:
        project.save_to_db()
        # except:
        #     return {"message": "An error occurred inserting the item."}, 500

        return project.json(), 201
