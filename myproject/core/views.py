import json
from myproject import db
from myproject.core.forms import SearchForm
from myproject.models import Rating,Recipes,Ingredient,Users
from flask import render_template, request, Blueprint,redirect, flash 
from sqlalchemy.orm import joinedload


core = Blueprint('core', __name__)
data = json.load(open('myproject/recipes/seed.json'))

@core.route('/', methods=['GET','POST'])
def index():
    #Adding search bar
    search =  SearchForm(request.form)
    return render_template('index.html', form=search)

@core.route('/search_recipe', methods=["GET","POST"])
def search():
    searchForm = SearchForm()
    recipes = Recipes.query.all()
    ingredients = Ingredient.query.all()
    results = []
    
    if request.method == "POST" and searchForm.validate_on_submit():
         for r in data['recipes']:
            if request.form['search'] == r['name']:
                results.append(r)
                return render_template('index.html',recipes=recipes, results=results, form=searchForm, data=data)
            else:
                pass
        
        #  return render_template('index.html',recipes=recipes, results=results, form=searchForm, data=data)
        
        # Working on adding in the ingredient search function, just added this but not getting the results I want.
    if request.method == "POST" and searchForm.validate_on_submit():
         for i in data['recipes']:
            if request.form['search'] == i['name']:
                results.append(i)
                return render_template('index.html',recipes=recipes, ingredients=ingredients, results=results, form=searchForm, data=data)
            else:
                pass
        
         return render_template('index.html',recipes=recipes, results=results, form=searchForm, data=data)

    return render_template('index.html',recipes=recipes, results=results, form=searchForm, data=data)
 ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
