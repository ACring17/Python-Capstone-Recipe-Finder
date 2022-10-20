# Where the blueprints will be registered
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

## Database Setup ##
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


## Login Configs ##
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'


from myproject.core.views import core
from myproject.users.views import users
from myproject.recipes.views import recipes
from myproject.ratings.views import ratings
from myproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(recipes)
app.register_blueprint(ratings)
app.register_blueprint(error_pages)
