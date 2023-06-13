import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database', 'instance', 'raspiFlaskVestal.db')

db = SQLAlchemy()


# Initialize SQLAlchemy with the Flask app
db.init_app(app)


from app import routes
