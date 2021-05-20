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


with open(os.path.join(sys.path[0], 'recipes.json'), 'r') as f:
    data = json.load(f)
    recipeKeys = [int(i) for i in list(data.keys())]


@app.route('/recipe/<number>')
def index(number):
    if number.isnumeric() and int(number) in recipeKeys:
        with open(os.path.join(sys.path[0], 'recipes.json'), 'r') as f:
            data = json.load(f)
        if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
            return data[str(number)]
        else:
            return '<!DOCTYPE html><html><head><title>Page Title</title></head><body>'+json2html.convert(json=data[str(number)])+'</body></html>'
    else:
        abort(400)


@app.route('/recipe/api/new', methods=['POST'])
def new():
    content = request.json
    with open(os.path.join(sys.path[0], 'recipes.json'), 'r+') as f:
        data = json.load(f)
        position = {str(max(recipeKeys)+1): content}
        data.update(position)
        recipeKeys.append(max(recipeKeys)+1)
        f.truncate(0)
        f.seek(0)
        json.dump(data, f)
    return jsonify({"id": max(recipeKeys)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
