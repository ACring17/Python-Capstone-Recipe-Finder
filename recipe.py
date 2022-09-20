from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True
    return render_template('index.html', user_logged_in=user_logged_in)

@app.route('/profile/<name>')
def profile(name):
    return f"User's profile: {name}"

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