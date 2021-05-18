from flask import Flask, request, jsonify, abort
import json
from json2html import *

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
        with open(number+'.json') as f:
            data = json.load(f)
        return json2html.convert(data)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
