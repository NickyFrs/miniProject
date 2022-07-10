from flask import (Blueprint, 
                   render_template, url_for, 
                   request, redirect, flash, session
                   )
from werkzeug.security import generate_password_hash, check_password_hash
from website.extensions import mongo, taskdb

main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html")


@main.route('/tasks')
def tasks():
    tasks =  taskdb.task.find()
    users = taskdb.users.find()
    return render_template("tasks.html", tasks=tasks, users=users)


@main.route('/login')
def login():
    return render_template("login.html")


@main.route('/profile')
def profile():
    return render_template("profile.html")


@main.route('/posts')
def posts():
    return render_template("posts.html")


@main.route('/newpost')
def newpost():
    return render_template("newpost.html")


@main.route('/logout')
def logout():
    return render_template("logout.html")


@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("first_name")
        lastName = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        # is user name exists
        userExist = taskdb.users.find_one(
            {"username": request.form.get('username')})
        
        userExist = taskdb.users.find_one(
            {"email" : request.form.get('email')})
        
        if userExist:
            flash("User already exists", category="error")
            return redirect(url_for('main.register'))
        
        if len(email) < 4:
            flash("email is too short, needs more than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("Name is too short, needs more than 2 characters", category="error")
        elif len(lastName) < 2:
            flash("Surname is too short, needs more than 2 characters", category="error")
        elif len(password1) < 8:
            flash("your password is too short, needs to be more than 8 characters", category="error")
        elif password1 != password2:
            flash("Password do not match, please try again", category="error")
        else:
            register = {
                "username" : request.form.get('username'),
                "email" : request.form.get('email'),
                "password" : generate_password_hash(request.form.get('password1')),
                "first_name" : request.form.get('first_name'),
                "last_name" : request.form.get('last_name'),
                }
            taskdb.users.insert_one(register)
            
            #start a session for the user
            session["users"] = request.form.get('username')
            flash("Registration Successful, account created. Thank you!", category="succsess")
            
    return render_template("register.html")