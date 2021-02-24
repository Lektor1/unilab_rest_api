from flask_restful import Resource, reqparse
from models.user import UserModel


class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="parameter 'username' must be in your request")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="parameter 'password' must be in your request")

    def post(self):
        data = RegisterUser.parser.parse_args()

        username_exists = UserModel.find_by_username(data['username'])

        if username_exists:
            return {"message": "This username already exists"}, 409

        user = UserModel(None, data['username'], data['password'])

        try:
            user.add()
            return {"message": "New user added"}, 200
        except Exception as err:
            return {"message": "An error acquired",
                    "error": err}, 500
