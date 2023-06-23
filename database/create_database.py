from app import app, db
from database import models

def create_tables():
    with app.app_context():
        for model in models:
            db.create_all()

if __name__ == '__main__':
    create_tables()
