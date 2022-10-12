from flask import Blueprint,render_template,redirect,url_for,request,redirect
from flask_login import current_user,login_required
from myproject import db
from myproject.models import Recipes
from myproject.recipes.forms import SearchRecipe,AddRecipeForm,UpdateRecipeForm,DelRecipeForm

recipes = Blueprint('recipes',__name__)

@recipes.route('/create', methods=['GET', 'POST'])
@login_required
def create_recipe():
    form = AddRecipeForm()

    if form.validate_on_submit():
        recipe = Recipes(name=form.name.data,
                        direction=form.direction.data,
                        user_id=current_user.id)

        # Add new Recipe to database
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('add.html',form=form) #Left off here, need to make sure template is created

@recipes.route('/list')
def list():
    # Grab a list of recipes from database.
    recipes = Recipes.query.all()
    return render_template('list.html', recipes=recipes)

@recipes.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelRecipeForm()

    if form.validate_on_submit():
        id = form.id.data
        recipe = Recipes.query.get(id)
        db.session.delete(recipe)
        db.session.commit()

        return redirect(url_for('recipes.list'))
    return render_template('delete.html',form=form)


@recipes.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateRecipeForm()

    if form.validate_on_submit():
        name = form.name.data

        # Update new Recipe to database
        new_recipe = Recipes(name)
        db.session.add(new_recipe)
        db.session.commit()

        return redirect(url_for('recipes.list'))

    return render_template('add.html',form=form)