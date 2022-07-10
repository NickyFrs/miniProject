# Imports
from flask import Flask
from main import main
from .extensions import DBNAME, mongo, db


def create_app(config_object='website.settings'):
    app = Flask(__name__)
    
    # app configurations
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'squlite:///{DBNAME}'
    
    # initializations    
    mongo.init_app(app)
    # db.init_app(app)
    
    # blueprint configuration
    app.register_blueprint(main)
    
    return app