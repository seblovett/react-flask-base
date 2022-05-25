import time
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/time')
class getTime(Resource):
    def get(self):
        return {'time': time.time()}