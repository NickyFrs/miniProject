import os
from flask_pymongo import PyMongo, MongoClient
from flask_sqlalchemy import SQLAlchemy

cluster = MongoClient("mongodb+srv://dbAuth:Ch3rl1na10@cluster0.rqlwn.mongodb.net/?retryWrites=true&w=majority")



mongo = PyMongo()
taskdb = cluster["task_manager"]
db = SQLAlchemy
DBNAME = "database.db"