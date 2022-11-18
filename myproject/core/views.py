import json
from myproject import db
from myproject.core.forms import SearchForm
from myproject.models import Rating,Recipes,Ingredient,Users
from flask import render_template, request, Blueprint,redirect, flash 
from sqlalchemy.orm import joinedload


core = Blueprint('core', __name__)
data = json.load(open('../recipes/seed.json'))

@core.route('/', methods=['GET','POST'])
def index():
    #Adding search bar
    search =  SearchForm(request.form)
    return render_template('index.html', form=search)

@core.route('/search_recipe', methods=["GET","POST"])
def search():
    searchForm = SearchForm()
    recipes = Recipes.query.all()
    results = []
    
    if request.method == "POST" and searchForm.validate_on_submit():
         for r in data['recipes']:
            if request.form['Search'] == r['name']:
        
        print(results)
        # return results 
        return render_template('index.html',recipes=recipes, results=results, form=searchForm, data=data)
        
#Help in tango. I can't figure out how to get the search function to loop through json file.

 ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
