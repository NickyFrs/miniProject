import os
from flask_pymongo import PyMongo, MongoClient


cluster = MongoClient("mongodb+srv://dbAuth:Ch3rl1na10@cluster0.rqlwn.mongodb.net/?retryWrites=true&w=majority")


# MongDB database access
mongo = PyMongo()
taskdb = cluster["task_manager"]