import os

from pkg_resources import DEVELOP_DIST

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "NftRlbZHRMKWRtrXu8Me9ZrW5YnbXOCp")
os.environ.setdefault("MONGO_URI", "mongodb+srv://dbAuth:Ch3rl1na10@cluster0.rqlwn.mongodb.net/?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "task_manager")