from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '408573b3bb22fb76aa0c5ae611ffe5ab'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
#app.config["SQLALCHEMY_NATIVE_UNICODE"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from blogApp import routes