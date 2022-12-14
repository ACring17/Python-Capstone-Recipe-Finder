import json
from flask import Blueprint,render_template,redirect,url_for,request,redirect,abort
from flask_login import current_user,login_required
from myproject import db
from myproject.models import Recipes
from myproject.recipes.forms import AddRecipeForm,UpdateRecipeForm
from sqlalchemy.orm import joinedload



recipes = Blueprint('recipes',__name__)

#Create method
@recipes.route('/create', methods=['GET', 'POST'])
@login_required
def create_recipe():
    form = AddRecipeForm()

    if form.validate_on_submit():
        recipe = Recipes(name=form.name.data,
                        directions=form.directions.data,
                        user_id=current_user.id)

        # Add new Recipe to database
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('new_recipe.html',form=form) 

#View method
@recipes.route('/<int:recipes_id>')
def recipes_list(recipes_id):
    # Grab a list of recipes from database.
    recipes_list = Recipes.query.get_or_404(recipes_id)
    return render_template('recipe_rating.html', name=recipes_list.name, directions=recipes_list.direction)

#Delete Method
@recipes.route('/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipes.query.get_or_404(recipe_id)
    if recipe.rater != current_user:
        abort(403)

    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('core.index'))

#Update method
@recipes.route('/<int:recipe_id>/update', methods=['GET', 'POST'])
@login_required
def update(recipe_id):
    recipe = Recipes.query.get_or_404(recipe_id)

    if recipe.rator != current_user:
        abort(403)

    form = UpdateRecipeForm()

    if form.validate_on_submit():
        recipe.name = form.name.data
        recipe.description = form.description.data
        recipe.directions = form.directions.data
        db.session.commit()

        return redirect(url_for('recipes.recipe', recipe_id=recipe.id))

    elif request.method == 'GET':
        form.name.data = recipe.name
        form.description = recipe.description
        form.directions = recipe.directions

    return render_template('core.index',form=form)

# Search query
# @recipes.route('/search', methods=['GET','POST'])
# def search(recipe):
#     Recipes.query.all()
#     all_recipes = Recipes.query.all()
#     for recipe in all_recipes:
#         #Think of how to get the results to render on home page
#         return render_template()

    #Loop through every recipe name
    #Recipe.query.all()
    #Loop through db and add to list of results
    #Might not need this code down below

    
        
        
        
        
        
