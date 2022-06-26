from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
# A file is needed to store the data (SQ lite 3)

def create_app():
    app = Flask(__name__) #initialise flask
    app.config['SECRET_KEY'] = 'i love NINTENDO' #whatever the KEY is equal to will be the secret key for the app
    #incript or secure the cookies and session data related to website 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # my SQLite or SQL alchemy database is stored/located at the location of f
    db.init_app(app) # take the defined db that this is the app that is going to be used 
    # when you want to store something in a database, you need to define the schema of what the object would look like = models.py

    
    from .views import views 
    from .auth import auth
    #from file import blueprint 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 
        #/ means no prefix 

    from .models import User, Note
    # Import the models file so that it defines the model classes 

    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    #where should flask redirect if the user is not logged in thus a login is required
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    #telling flask how to load a user. So what user we are looking for, looking for the user model and reference it by the ID

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    # Use path module to check if the database exists. If it does not exist, then create. 
    # We pass app as we need to tell flask SQLalchemy which app we are creating the database for 
    #the 'app' also has ['SQLALCHEMY_DATABASE_URI'] which tells us where to create the database 
    
