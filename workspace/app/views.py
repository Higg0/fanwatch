'''
Contains all of the site views. Basically a ToC.
This will be a lot of the meat of the app.
'''

from flask import render_template
from app import app


# Splash Screen
@app.route('/')
@app.route('/splash')
def splash():
    section='FanWatch'
    desc='Homepage the users first reach.'
    links=[['register','Register'],
           ['login','Login']]
    return render_template('sample_splash.html', section=section, desc=desc, links=links)

# Register
@app.route('/register')
def signup():
    section='Register'
    desc='Page to sign up for a new account.'
    links=[['','Back'],
           ['home','Register']]
    return render_template('sample_splash.html', section=section, desc=desc, links=links)
    
# Login
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
    
# View Events by Game
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
    