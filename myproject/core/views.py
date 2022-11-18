from myproject import db
from myproject.core.forms import SearchForm
from myproject.models import Rating,Recipes,Ingredient,Users
from flask import render_template, request, Blueprint,redirect, flash 

core = Blueprint('core', __name__)
data = db 

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
        recipes = data
        if recipes == data:
            results.append(recipes)
        else:
            Recipes.query.all()
        # results.append(recipes)
        print(results)
        # return results 
        return render_template('index.html',recipes=recipes, results=results, form=searchForm, data=data)
        # Current bug is sending name as search and not fetching data from JSON.


# ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
