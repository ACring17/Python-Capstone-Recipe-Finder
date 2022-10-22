#Where the models will be housed
from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin 

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True)
    name = db.Column(db.String(65),index=True)
    password_hash = db.Column(db.String(128))

    rated_recipes = db.relationship('Rating',backref='rater',lazy=True)#Hitting bug with connecting db when registering user

    def __init__(self,username,password,name):
        self.username = username
        self.name = name
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # String represenation of the db
    def __repr__(self):
        return f"Welcome {self.name} to Recipe Finder"

class Recipes(db.Model):

    __tablename__ = 'recipes'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    direction = db.Column(db.Text)
    


    def __init__(self,name,direction,description):
        self.name = name
        self.direction = direction

    def save_to_db(self):
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return f"Recipe name: {self.name}, Directions: {self.direction}"


class Ingredient(db.Model):

    __tablename__ = 'ingredients'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Indredients you have: {self.name}"


#Joining tables
class Rating(db.Model):

    __tablename__ = 'ratings'

    recipes = db.relationship(Recipes)
    user = db.relationship(Users)

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    rating_id = db.Column(db.Integer,primary_key=True)
    rating = db.Column(db.Integer)
    reveiw = db.Column(db.Text)

    def __init__(self,recipe_id,user_id,rating_id,rating,review):
        self.recipe_id = recipe_id
        self.user_id = user_id
        self.rating_id = rating_id
        self.rating = rating
        self.review = review

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Recipe:{self.recipe_id}, Rating: {self.rating}, Review:{self.review}"


class Measurement(db.Model):

    __tablename__ = 'measurements'

    recipes = db.relationship(Recipes)
    ingredients = db.relationship(Ingredient)

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'),nullable=False)
    ingredient_id = db.Column(db.Integer,db.ForeignKey('ingredients.id'),nullable=False)
    measurement_id = db.Column(db.Integer,primary_key=True)
    quantity = db.Column(db.Integer)

    def __init__(self,recipe_id,ingredient_id, measurement_id ,quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.measurement_id = measurement_id
        self.quantity = quantity

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f"Recipe:{self.recipe_id}, Ingredients:{self.ingredient_id}, Quantitity: {self.quantity}"

db.create_all()

#Seeding script ideas

#**** THINK THIS MIGHT BE THE ANSWER ******
# from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy.ext import mutable
# from flask import Flask

# app = Flask(__name__, template_folder="../templates")
# db = SQLAlchemy(app, session_options={'autocommit': True})

# class JsonEncodedDict(db.TypeDecorator):
#     """Enables JSON storage by encoding and decoding on the fly."""
#     impl = db.Text

#     def process_bind_param(self, value, dialect):
#         if value is None:
#             return '{}'
#         else:
#             return json.dumps(value)

#     def process_result_value(self, value, dialect):
#         if value is None:
#             return {}
#         else:
#             return json.loads(value)


# mutable.MutableDict.associate_with(JsonEncodedDict)

#***** FEELING GOOD ABOUT THIS METHOD   ****************
# import json

#@recie.route('/', methods=['GET', 'POST'])
#def seed():
    #if request.method == 'GET':
        #file = request.seed['seed']   

        #seed = Recipes(name=seed.name, direction=seed.direction)
        #db.session.add(seed)
        #db.session.commit()

    #return render_template(index.html)


#****** HELP ME VISUALIZE HOW TO HIT THE INFORMATION IN THE JSON FILE   *****************
# seed_recipe = Recipes(
#     name=json.loads(open('seed.json').read((''.join[1]['name']))),
#     direction=json.loads(open('seed.json').read('\n'.join([1]['steps']))),#'\n'.join(direction[1]['steps'])  This is how to get steps in terminal
# )

# #Attempt at looping through the script
# for name in seed_recipe:
#     return ''.join[0:]['name']

# try:
#     db.session.add(seed_recipe)
#     db.session.commit()
#     print('Insert successful')
# except:
#     print('Insert failed')


# seed_ingredient = Ingredient(
#     name=json.loads(open('seed.json').read('\n'.join([1]['ingredients'][0]['name'])))#Need all ingredients
# )

# #Attempt at looping through the script
# for name in seed_ingredient:
#     return ''.join[0:]['ingredients'][0:]['name']

# try:
#     db.session.add(seed_ingredient)
#     db.session.commit()
#     print('Insert successful')
# except:
#     print('Insert failed')


# seed_measurement = Measurement(
#     quantity=json.loads(open('seed.json').read('\n'.join([1]['ingredients'][0]['"quantity"'])))#Need all ingredient measurements
# )

# #Attempt at looping through the script
# for measurment in seed_measurement:
#     return ''.join[0:]['ingredients'][0:]['quantity']


# try:
#     db.session.add(seed_measurement)
#     db.session.commit()
#     print('Insert successful')
# except:
#     print('Insert failed')