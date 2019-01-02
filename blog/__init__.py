# blog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)


##################DataBase Setup#####################

basedir = os.path.abspath(os.path.dirname(__file__))

# Settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# Variables
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#######################################################

##################Login Setup#####################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.lonin_view = 'users.login'
#######################################################

from blog.core.views import core
from blog.users.views import users
from blog.posts.views import posts
from blog.error_pages.handlers import error_pages


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(error_pages)




