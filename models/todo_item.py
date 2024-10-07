from extensions import db
import datetime

class TodoItem(db.Model):

    __tablename__ = 'todo_item'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id