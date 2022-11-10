from myproject import db
from myproject.core.forms import SearchForm
from myproject.models import Rating,Recipes,Ingredient,Users
from flask import render_template, request, Blueprint,redirect, flash 

core = Blueprint('core', __name__)

@core.route('/', methods=['GET','POST'])
def index():
    #For showing reviews on the home page
    # page = request.args.get('page',1,type=int)
    # review=Rating.query.order_by(Rating.rating_id.desc()).paginate(page=page,per_page=20)
   
    #Adding search bar
    search =  SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@core.route('/<int:recipe_id>')
def search_results(recipe_id):
    recipe_result = Recipes.query.get_or_404(recipe_id)
    return render_template('index.html', name=recipe_result.name, directions=recipe_result.direction)


# ### Paths for the recipe and ingredients pages ###

# @core.route('/recipes')
# def recipes():
#     return render_template('recipes.html')

# @core.route('/ingredient')
# def ingredient():
#     return render_template('ingredient.html')
