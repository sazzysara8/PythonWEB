from . import db 
#from . means from this package, import the defined db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): # Database model is a layout or blueprint for an object that is going to be stored in my database = helps keep consistancy to data
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #Do not need to specify the date field ourselves, SQL alchemy would. func would get the current date and time
    # all notes must be associated for each user 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #foreignkey means that we must pass a valid ID of an existing user to this field/column when creating a new note. ('user.id') = id column of the User class
    # ForeignKey is Called "One to Many Relationship" where one user has many notes, and is only used when that relationship is valid 
    # Means that we can identify the user for every note that has been created by looking at the user ID


# - - - - - - - USER MODEL / DEFINED SCHEMA - What I want my User to store- - - - - - 

class User(db.Model, UserMixin): 
# when creating new model, define the name of the object 
    id = db.Column(db.Integer, primary_key=True)
    # primary_key is a unique identifier that represents an object. Totally unique. e.g) differentiate sames names   
    email = db.Column(db.String(150), unique=True)
    # String = state a length, Unique means that no user can have the same email as a different user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #List that will store the notes. able to access notes through this class 

# All columns I want to store
  