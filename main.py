# pip install flask
from flask import Flask
# pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# pip install flask_login
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# https://flask-login.readthedocs.io/en/latest/
# https://hackmd.io/@shaoeChen/ryvr_ly8f?type=view#note_1

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

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route("/")
def index():
	user01 = User.query.filter_by(username = 'Webb').first()
	# user01 = User.query.filter_by(username = 'Tom').first()
	if user01:
		login_user(user01)
		return "You are now logged in!"
	else:
		return "You need to log in!"

# Add a data into database
# Open Python3 Shell
# >>> from main import db, User
# >>> user1=User(username='Webb')
# >>> db.session.add(user1)
# >>> db.session.commit()
# Check it.
# >>> result=User.query.all()
# >>> result[0].username
# 'Webb'

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return "You are now logged out!"

@app.route("/home")
@login_required
def home():
	return "The current user is " + current_user.username 

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
