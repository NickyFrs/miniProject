from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo, MongoClient


# SQLAlchemy database access
sdb = SQLAlchemy()
DBNAME = "database.db"


# MongDB database access
cluster = MongoClient("mongodb+srv://dbAuth:Ch3rl1na10@cluster0.rqlwn.mongodb.net/?retryWrites=true&w=majority")

mongo = PyMongo()
taskdb = cluster["task_manager"]

