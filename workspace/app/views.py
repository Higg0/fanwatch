'''
Contains all of the site views. Basically a ToC.
This will be a lot of the meat of the app.
'''

from flask import render_template
from app import app

@app.route('/')
@app.route('/splash')
def splash():
    section='FanWatch'
    desc='Homepage the users first reach.'
    links=[['register','Register'],
           ['login','Login']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
@app.route('/register')
def signup():
    section='Register'
    desc='Page to sign up for a new account.'
    links=[['','Home']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
@app.route('/login')
def signin():
    section='Login'
    desc='Page to sign in to your account.'
    links=[['','Home']]
    return render_template('sample.html', section=section, desc=desc, links=links)