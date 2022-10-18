from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from myproject.models import Recipes, Ingredient

class SearchForm(FlaskForm):
    choices = [('Recipe', 'Recipe'),
               ('Ingredient', 'Ingredient')]
    select = SelectField('Search for recipe by:', choices=choices)
    search = StringField('')
    submit = SubmitField('Search') 