import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField#,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,TextField
from wtforms.validators import DataRequired
# Set up the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Configuring the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connecting the SQL
db = SQLAlchemy(app)

Migrate(app,db)

app.config['SECRET_KEY'] = 'mysecretkey'

class Recipes(db.Model):

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


# Form set up
class InfoForm(FlaskForm):
    firstname = StringField("First Name")
    lastname = StringField("Last Name")
    submit = SubmitField("Submit")

# Connecting the templates
@app.route('/')
def index():
    user_logged_in = True
    return render_template('index.html', user_logged_in=user_logged_in)

@app.route('/profile/<firstname>',methods=['GET','POST'])
def profile(name):
    firstname = False
    lastname = False
    form = InfoForm()
    # Functionality of the form data
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        form.firstname.data = ''
        form.lastname.data = ''
    return render_template('profile.html', form=form, firstname=firstname, lastname=lastname)

@app.route('/recipe/<search>')
def recipe(search):
    recipeList = []
    return f"Search for recipes: {search}"

@app.route('/ingredient/<search>')
def ingredient(search):
    ingredientList = []
    return f"Search for recipes by ingredient: {search}"

app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=False) #debug mode