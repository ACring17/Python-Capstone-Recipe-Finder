from flask import Flask

app =Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Recipe Finder!</h1>"

@app.route('/profile/<name>')
def profile(name):
    return f"User's profile: {name}"

@app.route('/recipe/<search>')
def recipe(search):
    return f"Search for recipes: {search}"

@app.route('/ingredient/<search>')
def ingredient(search):
    return f"Search for recipes by ingredient: {search}"


if __name__=='__main__':
    app.run(debug=False) #debug mode