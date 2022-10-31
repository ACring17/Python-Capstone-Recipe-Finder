from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from myproject.models import Recipes

class AddRecipeForm (FlaskForm):

    name = StringField('Name of your recipe?',validators=[DataRequired()])
    description = TextAreaField('Describe this dish.') 
    directions = TextAreaField('What are the Directions?',validators=[DataRequired()])
    submit = SubmitField('Update')
    
    def check_recipe(self,field):
        if Recipes.query.filter_by(name=field.data).first():
            raise ValidationError('Your recipe has been registered already!')

class UpdateRecipeForm(FlaskForm):

    name = StringField('username',validators=[DataRequired()])
    description = TextAreaField('Describe this dish.') 
    directions = TextAreaField('What are the Directions?',validators=[DataRequired()])
    submit = SubmitField('Update')

    def check_recipe(self,field):
        if Recipes.query.filter_by(name=field.data).first():
            raise ValidationError('Your recipe has been registered already!')
