import os

if os.path.exists("env.py"):
    import env

MONGO_URI = "mongodb+srv://nickyfrs:Cherlina#@cluster0.rqlwn.mongodb.net/?retryWrites=true&w=majority"
MONGO_DBNAME = os.environ.get("MONGO_DBNAME")
SECRET_KEY = os.environ.get("SECRET_KEY")
IP = os.environ.get("IP")
PORT =  os.environ.get("PORT")