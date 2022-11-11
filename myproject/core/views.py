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

@core.route('/<int:recipe_id>')
def search():
    searchForm = SearchForm()
    recipes = Recipes.query

    if searchForm.validate_on_submit():
        recipes = recipes.filter(Recipes.name.like('%' + searchForm.name.data + '%'))
        results = []
        recipes.append(results)
        db.session.add(results)
        db.session.commit()

    results = recipes.order_by(Recipes.name).all()

    return render_template('index.html', recipes=recipes, results=results)


# ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
