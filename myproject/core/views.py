from myproject.models import Rating
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    review=Rating.query.order_by(Rating.rating_id.desc()).paginate(page=page,per_page=20)
    return render_template('index.html',review=review)

@core.route('/recipes')
def recipes():
    return render_template('recipes.html')

@core.route('/ingredient')
def ingredient():
    return render_template('ingredient.html')

@core.route('/profile')
def profile():
    return render_template('profile.html')