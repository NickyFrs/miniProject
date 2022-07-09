from flask import render_template, request, redirect, url_for
from taskManager import app, db
from taskManager.models import Category, Task


@app.route("/")z
def home():
    return render_template("tasks.html", tasks=tasks)


