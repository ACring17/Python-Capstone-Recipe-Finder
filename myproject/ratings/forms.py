from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from myproject.models import Rating

class AddRatingForm (FlaskForm):

    rating = IntegerField('What would you rate this dish 1 - 5?', validators=[DataRequired()]) 
    review = TextAreaField('What did you think of this meal?',validators=[DataRequired()])
    submit = submit = SubmitField('Create Review')

    

class UpdateRatingForm(FlaskForm):

    rating = IntegerField('What would you rate this dish 1 - 5?', validators=[DataRequired()]) 
    review = TextAreaField('What did you think of this meal?',validators=[DataRequired()])
    submit = submit = SubmitField('Update')


