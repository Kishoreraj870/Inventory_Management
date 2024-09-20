from flask import Flask, jsonify, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import jwt
import datetime
from db import get_db
from flask import current_app as app
from models.users import User
from dotenv import load_dotenv
from flask import flash

bp = Blueprint('auth',__name__)
db=get_db()


# Registration Route
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input
    if not all(k in data for k in ('username', 'password', 'email')):
        return jsonify({'message': 'Missing fields'}), 400

    # Hash password
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    # Check if user already exists
    if db.users.find_one({'username': data['username']}):
        
        return jsonify({'message': 'Username already exists'}), 409

    user = {
        'username': data['username'],
        'email': data['email'],
        'password': hashed_password
    }
     
    db.users.insert_one(user)
    flash('USer registered successfully')
    return jsonify({'message': "User registered successfully"}), 201

# Login Route
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # print("data", data)
    password = data.get('password')

    # Validate input
    if not all(k in data for k in ('username', 'password')):
        return jsonify({'message': 'Missing fields'}), 400

    # Fetch the user from the database
    user = db.users.find_one({'username': data['username']})
    # # and check_password_hash(user['password'], data['password'])
    if user and check_password_hash(user["password"], password):
        token = jwt.encode({
        'username': user['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        flash('Login Successful')

        return jsonify({'token': token}), 200  # Return token as JSON
    
    return jsonify({'message': 'Invalid Credentials'}), 401


if __name__ == '__main__':
    app.run(debug=True)
