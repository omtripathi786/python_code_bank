from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        else:
            return {'error': 'Item not found'}

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item


api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
