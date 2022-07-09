from flask import render_template, request, redirect, url_for
from taskManager import app, db
from taskManager.models import Category, Task


@app.route("/")
@app.route("/get_task")
def get_task():
    return render_template("tasks.html", tasks=tasks)


