from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from flask_login import current_user
from myproject.models import Users

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In') 

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('pass_confirm', message="Passwords must match!")])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_username(self,field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username has been registered already!')

    
class UpdateUserForm(FlaskForm):

    username = StringField('username',validators=[DataRequired()])
    submit = SubmitField('Update')

    def check_username(self,field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username has been registered already!')