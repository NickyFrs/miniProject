from flask import Blueprint, render_template

from website.extensions import mongo, taskdb

main = Blueprint("main", __name__)


@main.route('/')
def tasks():
    tasks =  taskdb.task.find()
    return render_template("tasks.html", tasks=tasks)