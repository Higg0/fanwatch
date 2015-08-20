'''
Contains all of the site views. Basically a ToC.
This will be a lot of the meat of the app.
'''

from flask import Flask, render_template, flash, redirect, session, url_for, request, g, current_app
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from oauth import OAuthSignIn

from app import app, db, lm
from .models import User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

# Home Page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
# Authorize
@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

# Callback
@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, name=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))


#@login_required


'''
# Logged in homepage
@app.route('/me')
def me():
    return render_template('me_login.html')





@app.route('/login')
def signin():
    section='Login'
    desc='Page to sign in to your account.'
    links=[['','Back'],
           ['home','Login']]
    return render_template('sample_splash.html', section=section, desc=desc, links=links)
    
    

    
# Homepage
@app.route('/home')
def home():
    section='Home'
    desc='Homepage for logged in users.'
    links=[['events','Event'],
           ['sports','Pick a Sport'],
           ['venues','Pick a Venue']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
# Event Details
@app.route('/events')
def events():
    section='Event Details'
    desc='Details about a specific event.'
    links=[]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
# View Games by Sport
@app.route('/sports')
def sports():
    section='Sports'
    desc='List of sports/games to choose from.'
    links=[['games','Games']]
    return render_template('sample.html', section=section, desc=desc, links=links)

# View Events by Game
@app.route('/games')
def games():
    section='Games'
    desc='List of events to choose from.'
    links=[['new_event','Create New Event'],
           ['events','Select Event']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
# Create a new event
@app.route('/new_event')
def new_event():
    section='Create New Event'
    desc='Screen to create a new event.'
    links=[['events','See Event Details']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
# View Venues by Location
@app.route('/venues')
def venues():
    section='View list of venues by location.'
    desc='Screen to create a new event.'
    links=[['home','Home'],
           ['events','See Event Details']]
    return render_template('sample.html', section=section, desc=desc, links=links)

'''    