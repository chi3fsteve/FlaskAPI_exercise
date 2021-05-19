from flask import Flask, request, jsonify, abort
import json
from json2html import *
import os

app = Flask(__name__)


@app.errorhandler(400)
def bad_request(response):
    return jsonify(error=str(response)), 400

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': "405 Method Not Allowed"}), 405


@app.route('/')
def hello_world():
    return 'Hello, World!'


numbers = [1, 2, 3, 4]


@app.route('/recipe/<number>')
def index(number):
    if number.isnumeric() and int(number) in numbers:
        with open(os.path.join(sys.path[0], number+'.json'), 'r') as f:
            data = json.load(f)
        if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
            return data
        else:
            return json2html.convert(json=data)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
