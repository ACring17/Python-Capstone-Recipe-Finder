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
        recipes = searchForm.search#.filter(Recipes.name.like('%' + searchForm.name.data + '%'))    May not need this commented out part.
        results = []
        recipes.append(results)
        db.session.add(results)
        db.session.commit()

    results = recipes #Think how to access the results above and use them in the global sense
    print(results)

    return render_template('index.html', recipes=recipes, results=results, form=searchForm)


# ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
