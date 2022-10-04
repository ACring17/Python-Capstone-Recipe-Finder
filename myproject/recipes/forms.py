from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class SearchRecipe(FlaskForm):
    name = StringField('What recipe are you looking for?')
    search = SubmitField('Search')

class AddForm(FlaskForm):
    name = StringField('Name for your recipe?')
    submit = SubmitField('Add Recipe')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Recipe to Remove:')
    submit = SubmitField('Remove Recipe')
