from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# Hash = secure a password such that never storing password with plane text = want to convert to something that is more secure  
# A hashing function is a functyion that has no inverse. Meaning you can generate a hash with it. 
    # e.g) x → y (given x, it will always generate the same value y), but y → ? (given y, there is no way to find the value x)
    # Therefore, you can only check if the password you typed equals the hash that is stored. 
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# import jinja2_time
# from sympy import re

# from django.shortcuts import render
# from django.http import HttpResponse

# import os

auth = Blueprint('auth', __name__) #name of blueprint

@auth.route('/login', methods=['GET', 'POST']) 
#Now able to accept GET and POST requests from the routes
    # HTTP has different methods: get request, get method, post request, post method, put request, put method etc.
    # clearly distinguish between what type of request is being sent to your website 
    # Typically, Get request=loading a website. Post request= update or create - making some kind of change to the database or system (post the fact that we will signin or logout etc)
    # In form, I requested method=POST, we will send a request to the URL it is on. Hence the will send all information to the server 
        # server needs to interpret that, and respond or do something depending on the post request 
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
            # when looking for a specific entery in your database. Thus want to look by specific column or field
            #email=email means to filter all the users that have that email. first means to return the first result 
        if user: 
            #if a user is found from the email, then..
            if check_password_hash(user.password, password):
                #to check if the password that is inserted is equal to the hash that is stored
                #user.password - what ever user is found, we access with .password  
                #Hence, will hash the password inserted and check if against the user.password
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) #remember that the user is logged into the account while the web server is running
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')         
                
   # data = request.form #accessing the form atribute of request
   # print(data) #when there is data sent through "login", the data will show on the terminal as "ImmutableMultiDict"
    
    return render_template("login.html", user=current_user)
        #boolean=True #any variable, can access to in login.html (eg)text="testing", user="Sara" 



@auth.route('/logout')
@login_required #this route would make sure that we cannot access this page unless the user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()

        
# - - - - - - - Checking the validity of the submission - - - - - - -

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 9:
            flash('Email is invalid.', category='error') # visual message to user 
            pass
        elif len(first_name) < 3:
            flash('First name must be greater that 1 character', category='error')
            pass
        elif password1 != password2:
            flash('Passwords don\'t match. ', category='error')            
            pass
        elif len(password1) < 7:
            flash('Password must be at least 7 characters. ', category='error')            
            pass
        else: 
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))            
            db.session.add(new_user) # add new user to database
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            # add user to database
            return redirect(url_for('views.home'))
            # redirect to ('blueprintName.FunctionName)
        
        
    #How to get users information and store it in a database and create their user account.
    return render_template("sign_up.html", user=current_user)
    #When the page loads, it is a GET request, but when the page is submitted, it is a POST request

