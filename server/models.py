from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# Defining a model with Flask-SQLAlchemy requires a Python class with four key traits:

# Inheritance from the db.Model class.
# A __tablename__ class attribute.
# One or more class attributes assigned to the type db.Column.
# One class attribute specified to be the table's primary key.


# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
