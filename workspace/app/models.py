# Contains database structure (models)

from app import db

association_table = db.Table('association', db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True) 
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    created_events = db.relationship('Events', backref='creator', lazy='dynamic')

    # describes how to display objects in model
    def __repr__(self):
        return '<User %r>' % (self.nickname)
        
class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(120), index=True, unique=False) #combines team and venue
    venue_id = db.Column(db.String(120), index=True, unique=False) #pulled from Google Places API (exempt from caching restriction)
    game_id = db.Column(db.String(120), index=True, unique=False) #pulled from _____
    event_score = db.Column(db.Integer, unique=False) #calculated based on attendees
    attendees = db.relationship('User', secondary=association_table, backref=db.backref('events_attending', lazy='dynamic'))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # describes how to display objects in model
    def __repr__(self):
        return '<Events %r>' % (self.event_name)
        