from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SpringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    firstname = StringField("First Name")
    lastname = StringField("Last Name")
    submit = SubmitField("Submit")

@app.route('/')
def index():
    user_logged_in = True
    return render_template('index.html', user_logged_in=user_logged_in)

@app.route('/profile/<firstname>',methods=['GET','POST'])
def profile(name):
    firstname = False
    lastname = False
    form = InfoForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        form.firstname.data = ''
    return render_template('profile.html', form=form, firstname=firstname, lastname=lastname)

@app.route('/recipe/<search>')
def recipe(search):
    recipeList = []
    return f"Search for recipes: {search}"

@app.route('/ingredient/<search>')
def ingredient(search):
    ingredientList = []
    return f"Search for recipes by ingredient: {search}"

app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=False) #debug mode