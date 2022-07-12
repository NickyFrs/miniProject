# Imports
from os import path
from flask import Flask
from website.dbstore import DBNAME, sdb, mongo
from flask_login import LoginManager


def create_app(config_object='website.settings'):
    app = Flask(__name__)
    
    # app configurations
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DBNAME}'
    
    # initializations    
    mongo.init_app(app)
    sdb.init_app(app)
    
    # blueprint configuration
    # app.register_blueprint(main, url_prefix='/')
    # app.register_blueprint(main)
    from website.main.routes import main
    app.register_blueprint(main)

    
    # this will import all of the classes from the database
    from .models import Users, Notes, Posts
    
    # call the function to create the database
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'main.login' # where should the user be redirected if we are not logged in and a login is required
    login_manager.init_app(app) # initialize the login manager and tell it what app we are using
    
    # function to check the id of the user agains the db to load the user
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
    return app

"""
function to if the database exists 
and if it doesn't it creates it
"""
def create_database(app):
    if not path.exists('website/' + DBNAME):
        sdb.create_all(app=app)
        print('Database created successfully!')