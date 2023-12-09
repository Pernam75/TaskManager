from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
import regex

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
    
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def json(self):
        return {'id': self.id, 'title': self.title, 'done': self.done, 'user_id': self.user_id}
    
db.create_all()

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'Hello World!'}), 200)

@app.route('/users', methods=['POST'])
def create_user():
    print(request.get_json())
    try:
        inputs = request.get_json()
        existing_user = User.query.filter_by(email=inputs['email']).first()
        if existing_user:
            return make_response(jsonify({'error': 'user already exists'}), 500)
        # check if the email is in the right format
        if not regex.match(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$", inputs['email']):
            return make_response(jsonify({'error': 'email is not valid'}), 500)
        user = User(pseudo=inputs['pseudo'], email=inputs['email'], password=inputs['password'])
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 200)    
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
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
    
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        inputs = request.get_json()
        task = Tasks(title=inputs['title'], done=inputs['done'], user_id=inputs['user_id'])
        db.session.add(task)
        db.session.commit()
        return make_response(jsonify({'message': 'task created'}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Tasks.query.all()
        return make_response(jsonify({'tasks': [task.json() for task in tasks] if tasks else []}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    try:
        task = Tasks.query.filter_by(id=id).first()
        return make_response(jsonify({'task': task.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    try:
        inputs = request.get_json()
        task = Tasks.query.filter_by(id=id).first()
        task.title = inputs['title']
        task.done = inputs['done']
        task.user_id = inputs['user_id']
        db.session.commit()
        return make_response(jsonify({'message': 'task updated', 'task': task.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Tasks.query.filter_by(id=id).first()
        db.session.delete(task)
        db.session.commit()
        return make_response(jsonify({'message': 'task deleted', 'task': task.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
# get user tasks
@app.route('/users/<id>/tasks', methods=['GET'])
def get_user_tasks(id):
    try:
        tasks = Tasks.query.filter_by(user_id=id).all()
        return make_response(jsonify({'tasks': [task.json() for task in tasks]}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
