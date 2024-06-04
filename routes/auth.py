from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    user = User(name=data['name'], email=data['email'], password=hashed_password, city_id=data['city_id'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed'}), 401

    # For simplicity, we'll just return the user data, but in a real-world scenario, you should generate a token
    return jsonify({'user_id': user.id, 'name': user.name, 'email': user.email, 'city_id': user.city_id}), 200


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'user_id': user.id, 'name': user.name, 'email': user.email, 'city_id': user.city_id}), 200
