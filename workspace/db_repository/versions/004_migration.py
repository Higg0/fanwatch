#updating DB to remove many-to-many requirement...much more similar to original MockFlow breakdown

from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
association = Table('association', pre_meta,
    Column('user_id', Integer),
    Column('event_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String),
    Column('email', String),
    Column('first_name', String),
    Column('last_name', String),
)

attendees = Table('attendees', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_id', Integer),
    Column('user_id', Integer),
    Column('team_id', String(length=120)),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
)

events = Table('events', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_name', String),
    Column('venue_id', String),
    Column('game_id', String),
    Column('event_score', Integer),
    Column('creator_id', Integer),
)

events = Table('events', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_name', String(length=120)),
    Column('venue_id', String(length=120)),
    Column('game_id', String(length=120)),
    Column('creator_id', Integer),
    Column('home_team_name', String(length=120)),
    Column('away_team_name', String(length=120)),
    Column('date', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['association'].drop()
    pre_meta.tables['user'].drop()
    post_meta.tables['attendees'].create()
    post_meta.tables['users'].create()
    pre_meta.tables['events'].columns['event_score'].drop()
    post_meta.tables['events'].columns['away_team_name'].create()
    post_meta.tables['events'].columns['date'].create()
    post_meta.tables['events'].columns['home_team_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['association'].create()
    pre_meta.tables['user'].create()
    post_meta.tables['attendees'].drop()
    post_meta.tables['users'].drop()
    pre_meta.tables['events'].columns['event_score'].create()
    post_meta.tables['events'].columns['away_team_name'].drop()
    post_meta.tables['events'].columns['date'].drop()
    post_meta.tables['events'].columns['home_team_name'].drop()
