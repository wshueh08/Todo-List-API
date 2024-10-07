#Instantiate the necessary tools (such as a database and JWT authentication manager) to make them easily accessible throughout the entire application

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()