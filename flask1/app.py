from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask("Flick Finder") 
api = Api(app)

# Hardcoded database
data = {}

# Request parser
parser = reqparse.RequestParser()
parser.add_argument('data', type=str, help='Data to be stored')

# GET, PUT, and DELETE operations
class DataResource(Resource):
    def get(self, key):
        if key in data:
            return {key: data[key]}
        else:
            abort(404, message="Data not found")


    def put(self, key):
        args = parser.parse_args()
        data[key] = args['data']
        return {key: data[key]}, 201

    def delete(self, key):
        if key not in data:
            abort(404, message="Data not found")
        del data[key]
        return '', 204

# POST service
class DataListResource(Resource):
    def post(self):
        args = parser.parse_args()
        key = str(len(data) + 1)
        data[key] = args['data']
        return {key: data[key]}, 201

api.add_resource(DataResource, '/data/<string:key>')
api.add_resource(DataListResource, '/data')

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask RESTful Example"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
