from myproject import db
from myproject.core.forms import SearchForm
from myproject.models import Rating,Recipes,Ingredient,Users
from flask import render_template, request, Blueprint,redirect, flash 

core = Blueprint('core', __name__)

@core.route('/', methods=['GET','POST'])
def index():
    page = request.args.get('page',1,type=int)
    review=Rating.query.order_by(Rating.rating_id.desc()).paginate(page=page,per_page=20)
   
    #Adding search bar
    search =  SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html',review=review, form=search)

@core.route('/results')
def search_results(search):
    form = SearchForm
    results = []
    search_string = search.data['search']
    if search_string == '':
        qry = db.session.query(Recipes)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('index.html', results=results, form=form)


@core.route('/recipes')
def recipes():
    return render_template('recipes.html')

@core.route('/ingredient')
def ingredient():
    return render_template('ingredient.html')
