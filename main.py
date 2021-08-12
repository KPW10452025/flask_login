# pip install flask
from flask import Flask
# pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# pip install flask_login
from flask_login import LoginManager, UserMixin
# https://flask-login.readthedocs.io/en/latest/

import os
# pip install python-dotenv
# Put the environment variables at .env file.
# Use dotenv to receive the environment variables.
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
# Open Python3 Shell, and create the database.
# >>> from main import db
# >>> db.create_all()
# >>> quit()

# Check the table if exusts or not.
# Type in sqlite3 app.db at terminal.
# sqlite> .table
# user
# sqlite> .quit
