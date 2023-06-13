from flask_sqlalchemy import SQLAlchemy
from app import db

# Define the model for the "tempsys" table
class Tempsys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String)
    tempC = db.Column(db.Float)
    tempF = db.Column(db.Float)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
