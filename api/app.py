from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def json(self):
        return {'id': self.id, 'pseudo': self.pseudo, 'email': self.email, 'password': self.password}
    
db.create_all()

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'Hello World!'}), 200)

@app.route('/users', methods=['POST'])
def create_user():
    print(request.get_json())
    try:
        inputs = request.get_json()
        user = User(pseudo=inputs['pseudo'], email=inputs['email'], password=inputs['password'])
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 200)    
    except Exception as e:
        return make_response(jsonify({'error': 'aie' + str(e)}), 500)
    
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify({'users': [user.json() for user in users]}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        return make_response(jsonify({'user': user.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        inputs = request.get_json()
        user = User.query.filter_by(id=id).first()
        user.pseudo = inputs['pseudo']
        user.email = inputs['email']
        user.password = inputs['password']
        db.session.commit()
        return make_response(jsonify({'message': 'user updated', 'user': user.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'user deleted', 'user': user.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)