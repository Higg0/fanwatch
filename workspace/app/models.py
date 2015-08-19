# Contains database structure (models)

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    created_events = db.relationship('Events', backref='creator', lazy='dynamic') #user.created_events should allow us to find events they have created

    # describes how to display objects in model
    def __repr__(self):
        return '<User %r>' % (self.name)

class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(120), index=True, unique=False) #combines team and venue, format - 'League_HomeTeam_AwayTeam_VenueName'
    venue_id = db.Column(db.String(120), index=True, unique=False) #reference token pulled from Google Places API (exempt from caching restriction)
    game_id = db.Column(db.String(120), index=True, unique=False) #pulled from _____ (need to figure this out), pull home / away IDs and names from here
    date = db.Column(db.String(120), index=True, unique=False) #format is YYYYMMDD
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # describes how to display objects in model
    def __repr__(self):
        return '<Events %r>' % (self.event_name)
        
class Attendees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    team_id = db.Column(db.String(120), index=True, unique=False) #get from game_id API pull (when users select one of the 2)
    
    # describes how to display objects in model
    def __repr__(self):
        return '<Attendees %r>' % (self.user_id)
    
    #note - event score values are calculated in an algorithm pulled from Attendees