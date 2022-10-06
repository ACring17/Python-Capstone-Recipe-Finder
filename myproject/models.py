#Where the models will be housed
from enum import unique
from myproject import db,login_manager
from myproject.core.views import index
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Users(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True)
    name = db.Column(db.String(65),index=True)
    password_hash = db.Column(db.String(128))

    rated_recipes = db.relationship('Recipes',backref='rater',lazy=True)

    def __init__(self,username,password,name):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.name = name

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    # String represenation of the db
    def __repr__(self):
        return f"Welcome {self.name} to Recipe Finder"

class Recipes(db.Model):

    __tablename__ = 'recipes'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    direction = db.Column(db.Text)
    description = db.Column(db.Text)


    def __init__(self,name,direction,description):
        self.name = name
        self.description = description
        self.direction = direction

    def __repr__(self):
        return f"Recipe name: {self.name}, Description: {self.description}, Directions: {self.direction}"


class Ingredient(db.Model):

    __tablename__ = 'ingredients'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Indredients you have: {self.name}"


#Joining tables
class Rating(db.Model):

    __tablename__ = 'ratings'

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'),nullable=False)
    ingredient_id = db.Column(db.Integer,db.ForeignKey('ingredients.id'),nullable=False)
    rating = db.Column(db.Integer)
    reveiw = db.Column(db.Text)

    def __init__(self,recipe_id,ingredient_id,rating,review):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.rating = rating
        self.review = review

    def __repr__(self):
        return f"Recipe:{self.recipe_id}, Ingredients:{self.ingredient_id}, Rating: {self.rating}, Review:{self.review}"


class Measurement(db.Model):

    __tablename__ = 'measurements'

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'),nullable=False)
    ingredient_id = db.Column(db.Integer,db.ForeignKey('ingredients.id'),nullable=False)
    quantity = db.Column(db.Integer)

    def __init__(self,recipe_id,ingredient_id,quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity

    def __repr__(self):
        return f"Recipe:{self.recipe_id}, Ingredients:{self.ingredient_id}, Quantitity: {self.quantity}"