from flask_restful import Resource, reqparse
from models.user import UserModel
from oauth2client import client, crypt


class GoogleSignUp(Resource):
    """
    Class handling all google oauth user signups.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('id_token',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = GoogleSignUp.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        client_id = '468635640034-rp3e0rdggu885nbvtjvtis70u7g7vt1h.apps.googleusercontent.com'
        idinfo = client.verify_id_token(data['id_token'], client_id)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
        user = UserModel(username=data['username'], oauth=True)
        user.save_to_db()

        return user.json(), 201


class UserRegister(Resource):
    """
    Class handling all user signups.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return user.json(), 201


class Users(Resource):
    """
        Class that handles get requests for all users.
    """
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}
