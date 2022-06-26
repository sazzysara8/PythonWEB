#Store standart routes for the website 
#where users can access to (home page)
 
from cgitb import html
from django.urls import path
from flask import Flask, Blueprint, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
#current user detects whether the user is logged in. If logged in, atributes: name, notes, email. can be accessed  
from .models import Note
from . import db
import json

# import base64
# from PIL import Image
# import io



#define blueprint
#blueprint - has routes, URLs. separate and organise

views = Blueprint('views', __name__) #name of blueprint


@views.route('/', methods=['GET'])
@login_required  
def home(): 
    homeimg = url_for('static', filename='Homeimg/homeimg.jpg')
    homeCSS = url_for('static', filename='CSS/home.css')
    return render_template("home.html", 
                           homeimg=homeimg, 
                           homeCSS=homeCSS, 
                           user=current_user)


@views.route('/noting', methods=['GET','POST'])
@login_required  
#name of Blueprint 
def noting():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 2:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            
    return render_template("noting.html", user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Look for the noteId that was sent to us
    note = json.loads(request.data) #brought from JS　
    # going to take in data from a post request and load it as a Json object 
    noteId = note['noteId']
    # Then going to access the note ID attribute (in JS:{ noteId: noteId })
    note = Note.query.get(noteId)
    # Note.query.get will look for the note that has the same ID, then check if it exists  
    if note: 
        if note.user_id == current_user.id:
            # If the note exists thus is owned by the user (security check)
            db.session.delete(note)
            # Then will delete the note 
            db.session.commit()
    
    return jsonify({})

    # Then return an empty response as something needs to be responded in flask



@views.route('/aboutme', methods=['GET'])
def aboutme():
    #path is filename string
    drawing = url_for('static', filename='aboutmeimg/drawing.JPG')
    food = url_for('static', filename='aboutmeimg/food.jpg')
    NY = url_for('static', filename='aboutmeimg/NY.jpg')
    photography = url_for('static', filename='aboutmeimg/photography.jpg')
    
    aboutmeCSS = url_for('static', filename='CSS/aboutme.css')

    return render_template('aboutme.html', 
                           drawing=drawing, 
                           food=food,
                           NY=NY,
                           photography=photography,
                           aboutmeCSS=aboutmeCSS
                           )
    
    
    
@views.route('/photogallery', methods=['GET'])
def photogallery():
    #path is filename string
    GC = url_for('static', filename='photogalleryimg/GC.JPG')
    GC2 = url_for('static', filename='photogalleryimg/GC2.JPG')
    GC3 = url_for('static', filename='photogalleryimg/GC3.JPG')
    GC4 = url_for('static', filename='photogalleryimg/GC4.JPG')
    NBN = url_for('static', filename='photogalleryimg/NBN.JPG')
    NBN2 = url_for('static', filename='photogalleryimg/NBN2.JPG')
    NBN3 = url_for('static', filename='photogalleryimg/NBN3.JPG')
    NBN4 = url_for('static', filename='photogalleryimg/NBN4.JPG')
    NF = url_for('static', filename='photogalleryimg/NF.JPG')
    NF2 = url_for('static', filename='photogalleryimg/NF2.JPG')
    NF3 = url_for('static', filename='photogalleryimg/NF3.JPG')
    NF4 = url_for('static', filename='photogalleryimg/NF4.JPG')
    NFE = url_for('static', filename='photogalleryimg/NFE.JPG')
    NFN = url_for('static', filename='photogalleryimg/NFN.JPG')
    NFS = url_for('static', filename='photogalleryimg/NFS.JPG')
    SM = url_for('static', filename='photogalleryimg/SM.JPG')
    photogalleryCSS = url_for('static', filename='CSS/photogallery.css')

    return render_template('photogallery.html', 
                           GC=GC, GC2=GC2,GC3=GC3,GC4=GC4,
                           NBN=NBN,NBN2=NBN2,NBN3=NBN3,NBN4=NBN4,
                           NF=NF,NF2=NF2,NF3=NF3, NF4=NF4,
                           NFE=NFE,NFN=NFN,NFS=NFS,SM=SM,
                           photogalleryCSS=photogalleryCSS
                           )

@views.route('/traveling', methods=['GET'])
def traveling():
    H1 = url_for('static', filename='travelingimg/H1.JPG')
    H2 = url_for('static', filename='travelingimg/H2.JPG')
    H3 = url_for('static', filename='travelingimg/H3.JPG')
    H4 = url_for('static', filename='travelingimg/H4.JPG')
    H5 = url_for('static', filename='travelingimg/H5.JPG')
    H6 = url_for('static', filename='travelingimg/H6.JPG')
    H7 = url_for('static', filename='travelingimg/H7.JPG')
    H8 = url_for('static', filename='travelingimg/H8.JPG')
    H9 = url_for('static', filename='travelingimg/H9.JPG')
    H10 = url_for('static', filename='travelingimg/H10.JPG')
    H11 = url_for('static', filename='travelingimg/H11.JPG')
    H12 = url_for('static', filename='travelingimg/H12.JPG')
    H13 = url_for('static', filename='travelingimg/H13.png')
    H14 = url_for('static', filename='travelingimg/H14.JPG')
    H15 = url_for('static', filename='travelingimg/H15.png')
    H16 = url_for('static', filename='travelingimg/H16.JPG')
    H17 = url_for('static', filename='travelingimg/H17.JPG')
    H18 = url_for('static', filename='travelingimg/H18.png')
    
    travelingCSS = url_for('static', filename='CSS/traveling.css')
    return render_template('traveling.html',
                           H1=H1,H2=H2,H3=H3,H4=H4,H5=H5,H6=H6,
                           H7=H7,H8=H8,H9=H9, H10=H10,H11=H11,
                           H12=H12, H13=H13,H14=H14,H15=H15,
                           H16=H16,H17=H17,H18=H18,
                           travelingCSS=travelingCSS
                           )

@views.route('/food', methods=['GET'])
def food():
    #path is filename string
    f1 = url_for('static', filename='foodimg/21feb10.JPG')
    f2 = url_for('static', filename='foodimg/21jul7.JPG')
    f3 = url_for('static', filename='foodimg/21jun13-.JPG')
    f4 = url_for('static', filename='foodimg/21may13-.JPG')
    f5 = url_for('static', filename='foodimg/21may13.JPG')
    f6 = url_for('static', filename='foodimg/21may17.JPG')
    f7 = url_for('static', filename='foodimg/21nov13.JPG')
    f8 = url_for('static', filename='foodimg/21sep22.JPG')
    f9 = url_for('static', filename='foodimg/22apr4.png')
    f10 = url_for('static', filename='foodimg/22apr9-.JPG')
    f11 = url_for('static', filename='foodimg/22apr9.png')
    f12 = url_for('static', filename='foodimg/22apr17.png')
    f13 = url_for('static', filename='foodimg/22feb3.png')
    f14 = url_for('static', filename='foodimg/22feb3-.JPG')
    f15 = url_for('static', filename='foodimg/22feb8.JPG')
    f16 = url_for('static', filename='foodimg/22feb11.JPG')
    f17 = url_for('static', filename='foodimg/22feb18.JPG')
    f18 = url_for('static', filename='foodimg/22jan22.png')
    f19 = url_for('static', filename='foodimg/22mar3-.png')
    f20 = url_for('static', filename='foodimg/22mar3.png')
    f21 = url_for('static', filename='foodimg/22mar10-.png')
    f22 = url_for('static', filename='foodimg/22mar10.JPG')
    f23 = url_for('static', filename='foodimg/22mar13-.JPG')
    foodCSS = url_for('static', filename='CSS/food.css')

    return render_template('food.html', 
                           f1=f1,f2=f2,f3=f3,f4=f4,f5=f5,f6=f6,f7=f7,f8=f8,f9=f9,f10=f10,f11=f11,
                           f12=f12,f13=f13,f14=f14,f15=f15,f16=f16,f17=f17,f18=f18,f19=f19,
                           f20=f20,f21=f21,f22=f22,f23=f23,
                           foodCSS=foodCSS
                           )

@views.route('/drawing', methods=['GET'])
def drawing():
    #path is filename string
    e1 = url_for('static', filename='drawingimg/e1.JPG')
    e2 = url_for('static', filename='drawingimg/e2.JPG')
    e3 = url_for('static', filename='drawingimg/e3.JPG')
    e4 = url_for('static', filename='drawingimg/e4.JPG')
    e5 = url_for('static', filename='drawingimg/e5.JPG')
    e6 = url_for('static', filename='drawingimg/e6.JPG')
    e7 = url_for('static', filename='drawingimg/e7.JPG')
    e8 = url_for('static', filename='drawingimg/e8.JPG')
    e9 = url_for('static', filename='drawingimg/e9.JPG')
    e10 = url_for('static', filename='drawingimg/e10.JPG')
    e11 = url_for('static', filename='drawingimg/e11.JPG')
    drawingCSS = url_for('static', filename='CSS/drawing.css')

    return render_template('drawing.html', 
                           e1=e1,e2=e2,e3=e3,e4=e4,e5=e5, e6=e6,e7=e7,e8=e8,e9=e9,e10=e10,e11=e11,
                           drawingCSS=drawingCSS
                           )