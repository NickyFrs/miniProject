from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from taskManager import app, db
from taskManager.models import Category, Task


@app.route("/")
@app.route("/get_tatsk")
def get_task():
    task = mongo.db.task.find()
    return render_template("tasks.html", task=task) 


