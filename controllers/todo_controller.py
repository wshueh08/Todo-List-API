
from models.todo_item import TodoItem
from extensions import db


def create_todo_item(user_id, data):
    title = data.get('title')
    description = data.get('description')

    if not title:
        return {'message': 'Title is required'}, 400

    new_todo = TodoItem(title=title, description=description, user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()

    return {'id': new_todo.id, 'title': new_todo.title, 'description': new_todo.description}, 201


def update_todo_item(user_id, todo_id, data):

    todo = TodoItem.query.get_or_404(todo_id)

    if todo.user_id != user_id:
        return {'message': 'Forbidden'}, 403

    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    db.session.commit()

    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description
    }, 200


def delete_todo_item(user_id, todo_id):
   
    todo = TodoItem.query.get_or_404(todo_id)

    if todo.user_id != user_id:
        return {'message': 'Forbidden'}, 403

    db.session.delete(todo)
    db.session.commit()

    return '', 204

def get_user_todos(user_id):
    todos = TodoItem.query.filter_by(user_id=user_id).all()
    return [{'id': todo.id, 'title': todo.title, 'description': todo.description} for todo in todos]
