from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    #Will pass in data base list
    return render_template('index.html')

@core.route('/recipe')
def recipe():
    return render_template('recipe.html')

@core.route('/ingredient')
def recipe():
    return render_template('ingredient.html')

@core.route('/profile')
def recipe():
    return render_template('profile.html')