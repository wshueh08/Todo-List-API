from flask import Flask
from config import Config
from extensions import db, jwt
from models import User, TodoItem  
from routes import auth_bp, todo_bp 
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(todo_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Todo List API!"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

