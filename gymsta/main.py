from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if(current_user.is_authenticated):
        return redirect(url_for('main.profile'))
    return redirect(url_for('auth.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.nickname)

@main.route('/workouts')
@login_required
def workouts():
    return render_template('workouts.html')

@main.route('/exercises')
@login_required
def exercises():
    return render_template('exercises.html')

@main.route('/measurements')
@login_required
def measurements():
    return render_template('measurements.html')
