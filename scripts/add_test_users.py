from app import db, models

u = models.Users(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()

e = models.Events(event_name='NFL_Washington Nationals_Baltimore Orioles_Millers', venue_id=1234, game_id=4567, date = 20150727, creator_id=1)
db.session.add(e)
db.session.commit()

a = models.Attendees(event_id=1, user_id=1, team_id=91011)
db.session.add(a)
db.session.commit()