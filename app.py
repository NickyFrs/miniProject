import os
from flask import Flask, render_template, request
# if os.path.exists("env.py"):
#     import env


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
if os.environ.get('DEVELOPMENT') == True:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)
