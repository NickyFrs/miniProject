from flask import (Blueprint,
                   render_template, url_for,
                   request, redirect, flash, session
                   )
from werkzeug.security import generate_password_hash, check_password_hash
from website.dbstore import mongo, taskdb, sdb
from website.models import Users
from flask_login import login_user, login_required, logout_user, current_user

main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html")


@main.route('/tasks')
@login_required
def tasks():
    tasks = taskdb.task.find()
    users = taskdb.users.find()
    return render_template("tasks.html", user=current_user, tasks=tasks, users=users)


@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        userExist = taskdb.users.find_one(
            {"email": request.form.get('email')})

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("You are now logged in!", category="success")
                login_user(user, remember=True)
                return redirect(url_for('main.home'))
            else:
                flash("Incorrect password / login, please try again!", category="error")

        else:
            flash("Account does not exist, please register!", category="error")

    return render_template("login.html", user=current_user)


@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@main.route('/posts')
@login_required
def posts():
    return render_template("posts.html", user=current_user)


@main.route('/newpost')
@login_required
def newpost():
    return render_template("newpost.html", user=current_user)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # is username exists
        userExist = taskdb.users.find_one(
            {"username": request.form.get('username')})

        userExist = taskdb.users.find_one(
            {"email": request.form.get('email')})

        if userExist:
            flash("User already exists", category="error")
            return redirect(url_for('main.register'))

        user = Users.query.filter_by(email=email).first()
        if user:
            flash("Email already registered", category="error")
        if len(email) < 4:
            flash("email is too short, needs more than 4 characters", category="error")
        if len(username) < 5:
            flash("email is too short, needs more than 5 characters", category="error")
        elif len(first_name) < 4:
            flash("Name is too short, needs more than 4 characters", category="error")
        elif len(last_name) < 4:
            flash("Surname is too short, needs more than 4 characters", category="error")
        elif len(password1) < 5:
            flash("your password is too short, needs to be more than 5 characters", category="error")
        elif password1 != password2:
            flash("Password do not match, please try again", category="error")
        else:
            # Code to create a new use in the SQLAlchemy database
            create_user = Users(username=username, email=email, first_name=first_name, last_name=last_name,
                                password=generate_password_hash(password1, method="sha256"))
            sdb.session.add(create_user)
            sdb.session.commit()
            flash("Registration Successful, account created in database. Thank you!", category="succsess")

            # Code to create a new use in the MongoDB database
            register = {
                "username": request.form.get('username'),
                "email": request.form.get('email'),
                "password": generate_password_hash(request.form.get('password1')),
                "first_name": request.form.get('first_name'),
                "last_name": request.form.get('last_name'),
            }
            taskdb.users.insert_one(register)

            # start a session for the user
            session["users"] = request.form.get('username')
            login_user(current_user, remember=True)
            flash("Registration Successful, account created. Thank you!", category="succsess")
            return redirect(url_for('main.home'))

    return render_template("register.html", user=current_user)