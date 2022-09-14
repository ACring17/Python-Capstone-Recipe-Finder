from flask import Flask

app =Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Recipe Finder!</h1>"

@app.route('/profile')
def profile():
    return "User's profile"

@app.route('/recipe')
def recipe():
    return "Search for recipes"

@app.route('/ingredient')
def ingredient():
    return "Search for recipes by ingredient"


if __name__=='__main__':
    app.run()