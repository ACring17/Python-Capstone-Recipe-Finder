from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.ingredients.forms import AddForm,DelForm
from myproject.models import Ingredient

ingredients_blueprint = Blueprint('ingredients',
                              __name__,
                              template_folder='templates/ingredients')

@ingredients_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Recipe to database
        new_ingredient = Ingredient(name)
        db.session.add(new_ingredient)
        db.session.commit()

        return redirect(url_for('ingredients.list'))

    return render_template('add.html',form=form)

@ingredients_blueprint.route('/list')
def list():
    # Grab a list of ingredients from database.
    ingredients = Ingredient.query.all()
    return render_template('list.html', ingredients=ingredients)

@ingredients_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        ingredient = Ingredient.query.get(id)
        db.session.delete(ingredient)
        db.session.commit()

        return redirect(url_for('ingredients.list'))
    return render_template('delete.html',form=form)
