
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.todo_controller import (
    create_todo_item, 
    get_user_todos,
    update_todo_item,
    delete_todo_item
)


todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    user_id = get_jwt_identity()
    data = request.get_json()
    response, status = create_todo_item(user_id, data)
    return jsonify(response), status

@todo_bp.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    user_id = get_jwt_identity()
    response = get_user_todos(user_id)
    return jsonify({'data': response}), 200


@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo(todo_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    response, status = update_todo_item(user_id, todo_id, data)
    return jsonify(response), status


@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    user_id = get_jwt_identity()
    response, status = delete_todo_item(user_id, todo_id)
    return jsonify(response), status