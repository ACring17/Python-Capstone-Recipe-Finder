from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    #Will pass in data base list
    return render_template('index.html')

@core.route('/recipes')
def recipes():
    return render_template('recipes.html')

@core.route('/ingredient')
def ingredient():
    return render_template('ingredient.html')

@core.route('/profile')
def profile():
    return render_template('profile.html')