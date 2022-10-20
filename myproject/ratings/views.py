from flask import Blueprint,render_template,redirect,url_for,request,redirect
from flask_login import current_user,login_required
from myproject import db
from myproject.models import Rating
from myproject.ratings.forms import AddRatingForm,UpdateRatingForm

ratings = Blueprint('ratings',__name__,)

#Create method
@ratings.route('/add', methods=['GET', 'POST'])
@login_required
def create_rating():
    form = AddRatingForm()

    if form.validate_on_submit():
        rating = Rating(rating=form.rating.data,
                        review=form.review.data,
                        user_id=current_user.id)

        # Add new Recipe to database
        db.session.add(rating)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('ratings.html',form=form) 

#View method
@ratings.route('/<int:rating_id>')
def ratings_list():
    # Grab a list of ratings on recipes
    ratings_list = Rating.query.get_or_404(rating_id)
    return render_template('ratings.html', rating=ratings_list.rating,review=ratings_list.review)

@ratings.route('/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_rating(rating_id):
    rating = Rating.query.get_or_404(rating_id)
    if rating.rater != current_user:
        abort(403)

    db.session.delete(rating)
    db.session.commit()
    return redirect(url_for('core.index'))

#Update method
@ratings.route('/<int:rating_id>/update', methods=['GET', 'POST'])
@login_required
def update(rating_id):
    rating = Rating.query.get_or_404(rating_id)

    if rating.rator != current_user:
        abort(403)

    form = UpdateRatingForm()

    if form.validate_on_submit():
        rating.rating = form.rating.data
        rating.review = form.review.data
        db.session.commit()

        return redirect(url_for('ratings.rating', rating_id=rating.id))

    elif request.method == 'GET':
        form.rating = rating.rating
        form.review = rating.review

    return render_template('core.index',form=form)