from flask import Flask, request, jsonify, abort

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

@app.route('/product', methods=['POST'])
def index():
    if not request.is_json:
        abort(400, description='Not a JSON file')
    content = request.json
    if set(content.keys()) != {"token", "a", "b"}:
        abort(400, description='Wrong keys')
    if not all(isinstance(x, int) for x in list(content.values())):
        abort(400, description='Not all values are integers')
    if not all(x > 0 for x in list(content.values())):
        abort(400, description='Non positive integers are not allowed')
    return jsonify({"token": content["token"],
                    "product": content["a"] * content["b"]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
