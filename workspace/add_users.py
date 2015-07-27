from app import db, models

u = models.User(nickname='john', email='john@email.com', first_name='testfirst1', last_name='testlast1')
db.session.add(u)
db.session.commit()