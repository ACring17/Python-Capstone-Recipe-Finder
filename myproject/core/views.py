from myproject import db
from myproject.core.forms import SearchForm
from myproject.models import Rating,Recipes,Ingredient,Users
from flask import render_template, request, Blueprint,redirect, flash 

core = Blueprint('core', __name__)

@core.route('/', methods=['GET','POST'])
def index():
    #Adding search bar
    search =  SearchForm(request.form)
    return render_template('index.html', form=search)

@core.route('/search_recipe', methods=["POST"])
def search():
    print("here")
    searchForm = SearchForm()
    recipes = Recipes.query.all()

    if searchForm.validate_on_submit():
        recipes = searchForm.search
        results = []
        results.append(recipes)
        return results
        # db.session.add(results)  #moved bug down to here. Thinking I may not need the db storage for results.
        # db.session.commit()

    print(results)

    return render_template('index.html', recipes=recipes, results=results, form=searchForm)


# ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
