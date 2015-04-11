from flask.ext.security import Security, SQLAlchemyUserDatastore

from app import app
from db import db, User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

def create_user(username, email, password):
    user_datastore.create_user(username=username, email=email, password=password)
    db.session.commit()
    print("Session committed")
