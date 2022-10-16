from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from myproject.models import Rating

# class SearchRecipe(FlaskForm):
#     title = StringField('What recipe are you looking for?')
#     search = SubmitField('Search')
#     # Complete the search form --- May not need it here in ratings *****

class AddRatingForm (FlaskForm):

    rating = IntegerField('What would you rate this dish 1 - 5?', validators=[DataRequired()]) 
    review = TextAreaField('What did you think of this meal?',validators=[DataRequired()])
    submit = submit = SubmitField('Create Review')

    # def check_recipe(self,field):
    #     if Recipes.query.filter_by(name=field.data).first():
    #         raise ValidationError('Your recipe has been registered already!')

class UpdateRatingForm(FlaskForm):

    rating = IntegerField('What would you rate this dish 1 - 5?', validators=[DataRequired()]) 
    review = TextAreaField('What did you think of this meal?',validators=[DataRequired()])
    submit = submit = SubmitField('Update')


class DelRatingForm(FlaskForm):

    name = StringField('username',validators=[DataRequired()])
    submit = SubmitField('Remove Recipe')

    def check_recipe(self,field):
        if Rating.query.filter_by(name=field.data).first():
            raise ValidationError('Your recipe has been removed!')

#This maybe just a button instead