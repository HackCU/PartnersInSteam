from flask.ext.security import Security, SQLAlchemyUserDatastore

from app import app
from model import db, User, Role

user_datastore = SQLAlchemyUserDatastore(model.db, model.User, model.Role)
security = Security(app, user_datastore)
