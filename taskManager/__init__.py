import os
import re
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient

if os.path.exists("env.py"):
    import env  # moqa

def taskmanager():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.secret_key = os.environ.get("SECRET_KEY")
    
    return app
    
    # code to tell Heroku to change the uri name to postgresql
if os.environ.get("DEVELOPMENT") == "True":
    taskmanager.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    taskmanager.config["SQLALCHEMY_DATABASE_URI"] = uri  # Heroku
        
from .routes import routes 
    

db = SQLAlchemy(taskmanager)
mongo = PyMongo(db)
    
    

