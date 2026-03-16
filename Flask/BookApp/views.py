from . import app, db
from flask import render_template, redirect, url_for, flash
from .forms import RegistrationForm
from .models import Book, User
from werkzeug.security import generate_password_hash


@app.route("/")
def hello_world():
    books = Book.query.all()
    return render_template('home.html', books=books)


@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


@app.route('/catalogue')
def catalogue():
    books = Book.query.all()
    return render_template('catalogue.html', title='Catalogue', books=books)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        existing_user  = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash('Username already taken. Please choose another.', 'danger')
            return redirect(url_for('register'))

        if existing_email:
            flash('Email already registered. Please sign in.', 'danger')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(form.password.data)

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw
        )
        db.session.add(new_user)
        db.session.commit()

        flash(f'Account created for {form.username.data}! You can now log in.', 'success')
        return redirect(url_for('hello_world'))

    return render_template('register.html', title='Register', form=form)