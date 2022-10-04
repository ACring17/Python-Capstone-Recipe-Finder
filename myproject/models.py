#Where the models will be housed
from myproject import db 

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    name = db.Column(db.Text)

    def __init__(self,username,password,name):
        self.username = username
        self.password = password
        self.name = name
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

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'))
    ingredient_id = db.Column(db.Integer,db.ForeignKey('ingredients.id'))
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

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'))
    ingredient_id = db.Column(db.Integer,db.ForeignKey('ingredients.id'))
    quantity = db.Column(db.Integer)

    def __init__(self,recipe_id,ingredient_id,quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity

    def __repr__(self):
        return f"Recipe:{self.recipe_id}, Ingredients:{self.ingredient_id}, Quantitity: {self.quantity}"