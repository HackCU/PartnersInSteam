from flask.ext.security import Security, SQLAlchemyUserDatastore

from app import app
from model import db, User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
