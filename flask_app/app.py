from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

import oneagent
import oneagent.sdk as onesdk

if not oneagent.initialize():
    print('Error initializing OneAgent SDK.')

getsdk = oneagent.get_sdk

stores = [{
    'name': 'My Store',
    'items': [{'name': 'my item', 'price': 15.99}]
}]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store/', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'stores': stores})


@app.route('/store/<string:name>')
def get_store(name):
    sdk = getsdk()
    with sdk.trace_custom_service('my_fancy_transaction_new', 'MyFancyService_new'):
        for store in stores:
            if store['name'] == name:
                return jsonify(store)
        else:
            return jsonify({'Error:': 'store not found'})


@app.route('/stores/')
def get_stores():
    sdk = getsdk()

    with sdk.trace_custom_service('my_fancy_transaction', 'MyFancyService'):
        return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)

oneagent.shutdown()
