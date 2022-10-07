from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from myproject import db
from myproject.models import Users, Recipes, Ingredient, Rating, Measurement
from myproject.users.forms import RegistrationForm, LoginForm, UpdateUserForm

users = Blueprint('users',__name__)

# Register new user
@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = Users(username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)

# Login
@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = Users.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next ==None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
        
    return render_template('login.html',form=form)

# Logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

#User profile page
@users.route('/profile',methods=['GET','POST'])
@login_required
def profile():

    form = UpdateUserForm()
    if form.validate_on_submit():
        
        current_user.username = form.username.data
        db.session.commit()
        return redirect(url_for('users.profile'))
    
    elif request.method == "GET":
        form.username.data = current_user.username
        
    return render_template('profile.html',form=form)