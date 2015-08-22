'''
Contains all of the site views (basically a ToC)
'''

from flask import Flask, render_template, flash, redirect, session, url_for, request, g, current_app
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from oauth import OAuthSignIn
from content import get_sports, get_games

from app import app, db, lm
from .models import User, Events, Attendees
from .forms import SelectGame

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
    print username
    firstname=''
    if username != '':
        firstname=username.split()
        firstname=firstname[0]
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, name=username, email=email, firstname=firstname)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

# Create a new event - list of sports
@app.route('/new_event/sports')
@login_required
def create_pick_sport():
    section='Pick a sport'
    back=url_for('index')
    prompt='Pick a sport'
    listing=get_sports()
    return render_template('create_event_sports.html', section=section, back=back, listing=listing, prompt=prompt)

@app.route('/new_event/sports/<sport>', methods=['GET','POST'])
@login_required
def create_pick_game(sport):
    form=SelectGame()
    section='Pick a match'
    back=url_for('create_pick_sport')
    prompt='Pick a match'
    listing=get_games()
    if form.validate_on_submit():
        return redirect('/new_event/venue')
    return render_template('create_event_games.html', section=section, back=back, listing=listing, prompt=prompt, form=form)

@app.route('/new_event/venue')
@login_required
def create_event():
    section='Create Event'
    back=url_for('create_pick_sport')
    prompt='Pick a place'
    return render_template('sample.html', section=section, back=back, prompt=prompt)



# Lists events nearby in map
@app.route('/events')
@login_required
def events():
    section='Events'
    desc='Screen to create a new event.'
    links=[['events','See Event Details']]
    return render_template('sample.html', section=section, desc=desc, links=links)


'''

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

    
# View Venues by Location
@app.route('/venues')
def venues():
    section='View list of venues by location.'
    desc='Screen to create a new event.'
    links=[['home','Home'],
           ['events','See Event Details']]
    return render_template('sample.html', section=section, desc=desc, links=links)

'''    