from flask import Flask
from flask_restful import Api
from resources.bikes import BikeResources, BikeListResources
from flask_jwt import JWT
from security import authentication, identity
from resources.user import RegisterUser


app = Flask(__name__)
app.secret_key = "bike_key"
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"


api = Api(app)
jwt = JWT(app, authentication, identity)


@app.before_first_request
def create_table():
    db.create_all()


api.add_resource(BikeResources, "/bike/<string:bike_name>")
api.add_resource(BikeListResources, "/bikes")
api.add_resource(RegisterUser, "/registration")

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=5100, debug=True)