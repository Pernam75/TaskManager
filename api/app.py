from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'Hello World!'}), 200)