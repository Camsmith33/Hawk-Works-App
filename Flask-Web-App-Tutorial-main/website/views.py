from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import Drone_Log
from .models import Drone
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    logs = Drone_Log.query.all()  # Query all log entries
    return render_template("history.html", logs=logs, user=current_user) 

@views.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    return render_template("checkout.html", user=current_user)

@views.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    return render_template("checkin.html", user=current_user)

@views.route('/checklist', methods=['GET', 'POST'])
@login_required
def Labchecklist():
    return render_template("Labchecklist.html", user=current_user)

@views.route('/drone1_release', methods=['GET', 'POST'])
@login_required
def drone1_release():
    return render_template("drone1_release.html", user=current_user)

@views.route('/drone1_check', methods=['GET', 'POST'])
@login_required
def drone1_checkout():
    if request.method == 'POST':
        log = request.form.get('log')
        drone = Drone.query.filter_by(name="Drone 1").first()
        if drone and drone.status == "Available":
            new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 1", action="Check-out")  #providing the schema for the note 
            db.session.add(new_action) #adding the note to the database 
            drone.status = "Checked Out"
            db.session.commit()
            flash('Drone Checked-out!', category='success')
        else:
            flash('Drone Unavailable', category='error')
        db.session.commit()
    return render_template("drone1_check.html", user=current_user)

@views.route('/drone1_in', methods=['GET', 'POST'])
@login_required
def drone1_checkin():
    if request.method == 'POST':
        log = request.form.get('log')#Gets the note from the HTML
        drone = Drone.query.filter_by(name="Drone 1").first()
        if drone and drone.status == "Checked Out":
            if len(log) < 1:
                flash('Note is too short!', category='error') 
            else:
                new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 1", action="Check-in")  #providing the schema for the note 
                db.session.add(new_action) #adding the note to the database 
                drone.status = "Available"
                db.session.commit()
                flash('Drone Checked-in!', category='success')
        else:
            flash('Drone Already Checked-in', category='error')
        db.session.commit()
    return render_template("drone1_in.html", user=current_user)

@views.route('/drone2_release', methods=['GET', 'POST'])
@login_required
def drone2_release():
    return render_template("drone2_release.html", user=current_user)

@views.route('/drone2_check', methods=['GET', 'POST'])
@login_required
def drone2_checkout():
    if request.method == 'POST':
        log = request.form.get('log')
        drone = Drone.query.filter_by(name="Drone 2").first()
        if drone and drone.status == "Available":
            new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 2", action="Check-out")  #providing the schema for the note 
            db.session.add(new_action) #adding the note to the database 
            drone.status = "Checked Out"
            db.session.commit()
            flash('Drone Checked-out!', category='success')
        else:
            flash('Drone Unavailable', category='error')
        db.session.commit()
    return render_template("drone2_check.html", user=current_user)

@views.route('/drone2_in', methods=['GET', 'POST'])
@login_required
def drone2_checkin():
    if request.method == 'POST':
        log = request.form.get('log')#Gets the note from the HTML
        drone = Drone.query.filter_by(name="Drone 2").first()
        if drone and drone.status == "Checked Out":
            if len(log) < 1:
                flash('Note is too short!', category='error') 
            else:
                new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 2", action="Check-in")  #providing the schema for the note 
                db.session.add(new_action) #adding the note to the database 
                drone.status = "Available"
                db.session.commit()
                flash('Drone Checked-in!', category='success')
        else:
            flash('Drone Already Checked-in', category='error')
        db.session.commit()
    return render_template("drone2_in.html", user=current_user)

@views.route('/drone3_release', methods=['GET', 'POST'])
@login_required
def drone3_release():
    return render_template("drone3_release.html", user=current_user)

@views.route('/drone3_check', methods=['GET', 'POST'])
@login_required
def drone3_checkout():
    if request.method == 'POST':
        log = request.form.get('log')
        drone = Drone.query.filter_by(name="Drone 3").first()
        if drone and drone.status == "Available":
            new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 3", action="Check-out")  #providing the schema for the note 
            db.session.add(new_action) #adding the note to the database 
            drone.status = "Checked Out"
            db.session.commit()
            flash('Drone Checked-out!', category='success')
        else:
            flash('Drone Unavailable', category='error')
        db.session.commit()
    return render_template("drone3_check.html", user=current_user)

@views.route('/drone3_in', methods=['GET', 'POST'])
@login_required
def drone3_checkin():
    if request.method == 'POST':
        log = request.form.get('log')#Gets the note from the HTML
        drone = Drone.query.filter_by(name="Drone 3").first()
        if drone and drone.status == "Checked Out":
            if len(log) < 1:
                flash('Note is too short!', category='error') 
            else:
                new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 3", action="Check-in")  #providing the schema for the note 
                db.session.add(new_action) #adding the note to the database 
                drone.status = "Available"
                db.session.commit()
                flash('Drone Checked-in!', category='success')
        else:
            flash('Drone Already Checked-in', category='error')
        db.session.commit()
    return render_template("drone3_in.html", user=current_user)

@views.route('/drone4_release', methods=['GET', 'POST'])
@login_required
def drone4_release():
    return render_template("drone4_release.html", user=current_user)

@views.route('/drone4_check', methods=['GET', 'POST'])
@login_required
def drone4_checkout():
    if request.method == 'POST':
        log = request.form.get('log')
        drone = Drone.query.filter_by(name="Drone 4").first()
        if drone and drone.status == "Available":
            new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 4", action="Check-out")  #providing the schema for the note 
            db.session.add(new_action) #adding the note to the database 
            drone.status = "Checked Out"
            db.session.commit()
            flash('Drone Checked-out!', category='success')
        else:
            flash('Drone Unavailable', category='error')
        db.session.commit()
    return render_template("drone4_check.html", user=current_user)

@views.route('/drone4_in', methods=['GET', 'POST'])
@login_required
def drone4_checkin():
    if request.method == 'POST':
        log = request.form.get('log')#Gets the note from the HTML
        drone = Drone.query.filter_by(name="Drone 4").first()
        if drone and drone.status == "Checked Out":
            if len(log) < 1:
                flash('Note is too short!', category='error') 
            else:
                new_action = Drone_Log(note=log, full_name=current_user.full_name, drone="Drone 4", action="Check-in")  #providing the schema for the note 
                db.session.add(new_action) #adding the note to the database 
                drone.status = "Available"
                db.session.commit()
                flash('Drone Checked-in!', category='success')
        else:
            flash('Drone Already Checked-in', category='error')
        db.session.commit()
    return render_template("drone4_in.html", user=current_user)