import os
from pymongo import MongoClient
from flask import Flask
from flask_restful import Resource, Api, reqparse

# Instantiate the app
app = Flask(__name__)
api = Api(app)
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.calcdb

class listAll(Resource):
    def get(self):
        ret = []
        _items = db.calcdb.find().sort("km")
        items = [item for item in _items]
        count = 0;
        for item in items:
            ret.append([item['miles'], item['km'], item['location'], item['open']])
            count += 1;
        return { 'data': ret }

class listOpenOnly(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('top', type=int, location='args')
        args = parser.parse_args()
        ret = []
        _items = db.calcdb.find().sort("km")
        items = [item for item in _items]
        count = 0;
        for item in items:
            if count == args['top']:
                break
            ret.append([item['miles'], item['km'], item['location'], item['open']])
            count += 1;
        return { 'data': ret }

class listCloseOnly(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('top', type=int, location='args')
        args = parser.parse_args()
        ret = []
        _items = db.calcdb.find().sort("km")
        items = [item for item in _items]
        count = 0;
        for item in items:
            if count == args['top']:
                break
            ret.append([item['miles'], item['km'], item['location'], item['close']])
            count += 1;
        return { 'data': ret }

class listAllcsv(Resource):
    def get(self):
        ret = []
        _items = db.calcdb.find().sort("km")
        items = [item for item in _items]
        count = 0;
        for item in items:
            ret.append([item['miles'], item['km'], item['location'], item['open']])
            retstr = ','.join(map(str,ret))
            count += 1;
        return { 'data': retstr }

class listOpenOnlycsv(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('top', type=int, location='args')
        args = parser.parse_args()
        ret = []
        _items = db.calcdb.find().sort("km")
        items = [item for item in _items]
        count = 0;
        for item in items:
            if count == args['top']:
                break
            ret.append([item['miles'], item['km'], item['location'], item['open']])
            retstr = ','.join(map(str,ret))
            count += 1;
        return { 'data': retstr }

class listCloseOnlycsv(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('top', type=int, location='args')
        args = parser.parse_args()
        ret = []
        _items = db.calcdb.find().sort("km")
        items = [item for item in _items]
        count = 0;
        for item in items:
            if count == args['top']:
                break
            ret.append([item['miles'], item['km'], item['location'], item['close']])
            retstr = ','.join(map(str,ret))
            count += 1;
        return { 'data': retstr }
# Create routes
# Another way, without decorators
api.add_resource(listAll, '/', '/listAll', '/listAll/json')
api.add_resource(listOpenOnly, '/listOpenOnly', '/listOpenOnly/json')
api.add_resource(listCloseOnly, '/listCloseOnly', '/listCloseOnly/json')

api.add_resource(listAllcsv, '/listAll/csv')
api.add_resource(listOpenOnlycsv, '/listOpenOnly/csv')
api.add_resource(listCloseOnlycsv, '/listCloseOnly/csv')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)