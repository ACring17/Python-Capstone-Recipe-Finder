from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class SearchIngredient(FlaskForm):
    name = StringField('What ingredient are you looking for?')
    search = SubmitField('Search')

class AddForm(FlaskForm):
    name = StringField('Name for your ingredient?')
    submit = SubmitField('Add ingredient')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of ingredient to Remove:')
    submit = SubmitField('Remove ingredient')
