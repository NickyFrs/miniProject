from flask import (Blueprint, 
                   render_template, 
                   request, redirect, flash
                   )

from website.extensions import mongo, taskdb

main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html")


@main.route('/tasks')
def tasks():
    tasks =  taskdb.task.find()
    return render_template("tasks.html", tasks=tasks)


@main.route('/login')
def login():
    return render_template("login.html")


@main.route('/register')
def register():
    return render_template("register.html")