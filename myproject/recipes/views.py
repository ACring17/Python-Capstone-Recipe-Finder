from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.recipes.forms import AddForm,DelForm
from myproject.models import Recipes

puppies_blueprint = Blueprint('recipes',
                              __name__,
                              template_folder='templates/recipes')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Recipe to database
        new_recipe = Recipes(name)
        db.session.add(new_recipe)
        db.session.commit()

        return redirect(url_for('recipes.list'))

    return render_template('add.html',form=form)

@recipes_blueprint.route('/list')
def list():
    # Grab a list of recipes from database.
    puppies = Puppy.query.all()
    return render_template('list.html', recipes=recipes)

@recipes_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Recipes.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('recipes.list'))
    return render_template('delete.html',form=form)
