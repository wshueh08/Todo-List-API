from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user import User
from extensions import db

def register_user(data):
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return {'message': 'Missing required fields'}, 400

    if User.query.filter_by(email=email).first():
        return {'message': 'Email already exists'}, 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    token = create_access_token(identity=new_user.id)
    return {'token': token}, 201


def login_user(data):
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        token = create_access_token(identity=user.id)
        return {'token': token}, 200

    return {'message': 'Invalid credentials'}, 401
