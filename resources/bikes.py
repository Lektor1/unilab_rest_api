from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.bikes import BikeModel


class BikeListResources(Resource):

    def get(self):

        bike_dict = {}
        bike_list = BikeModel.get_all_bikes()

        for bike in bike_list:
            temp = {
                "name": bike.name,
                "size": bike.size,
                "price": bike.price
            }
            bike_dict[bike.bike_id] = temp

        if bike_list:
            return bike_dict, 200
        else:
            return {"message": "List of bikes is empty or not found"}, 404

    @jwt_required()
    def delete(self):
        bike_list = BikeModel.get_all_bikes()

        if bike_list:
            BikeModel.delete_all_rows()
            return {"message": "all Bikes deleted"}, 200
        else:
            return {"message": "Table is empty"}, 404


class BikeResources(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('size',
                        type=str,
                        required=True,
                        help="parameter 'size' must be in your request")
    parser.add_argument('price',
                        type=int,
                        required=True,
                        help="parameter 'price' must be in your request")

    @jwt_required()
    def get(self, bike_name):
        bike_data = BikeModel.find_by_name(bike_name)

        if bike_data:
            return bike_data.json(), 200
        return {"message": "Bike with this name not found"}, 404

    @jwt_required()
    def post(self, bike_name):

        if BikeModel.find_by_name(bike_name):
            return {"message": "Bike with this name already exists"}, 409

        data = BikeResources.parser.parse_args()

        bike = BikeModel(None, bike_name, data['size'], data['price'])

        try:
            bike.save_to_db()
            return {"message": "New bike added"}, 200
        except Exception as err:
            return {"message": "An error acquired",
                    "error": err}, 500

    @jwt_required()
    def put(self, bike_name):

        bike = BikeModel.find_by_name(bike_name)
        data = BikeResources.parser.parse_args()

        if bike:
            bike.size = data['size']
            bike.price = data['price']
        else:
            bike = BikeModel(None, bike_name, data['size'], data['price'])

        bike.save_to_db()
        return bike.json()

    @jwt_required()
    def delete(self, bike_name):

        bike = BikeModel.find_by_name(bike_name)

        if bike:
            bike.delete_from_db()
            return {"message": "bike deleted"}, 200
        return {"message": "Bike with this id not found"}, 404
