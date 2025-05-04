from forum import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from flask_login import current_user, login_required, login_user, logout_user
from .model import User
from time import sleep

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You are already registered")
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Successfully Registered!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.")
        return redirect(url_for('dashboard'))  
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        flash("Invalid username or password.")
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
        