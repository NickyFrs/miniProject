import os
from flask_pymongo import PyMongo, MongoClient

custer = MongoClient("mongodb+srv://dbAuth:Ch3rl1na10@cluster0.rqlwn.mongodb.net/?retryWrites=true&w=majority")



mongo = PyMongo()
taskdb = custer["task_manager"]