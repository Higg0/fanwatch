#slight update to events (removed home/away and placed with evene_name)

from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
events = Table('events', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_name', String),
    Column('venue_id', String),
    Column('game_id', String),
    Column('creator_id', Integer),
    Column('away_team_name', String),
    Column('date', String),
    Column('home_team_name', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['events'].columns['away_team_name'].drop()
    pre_meta.tables['events'].columns['home_team_name'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['events'].columns['away_team_name'].create()
    pre_meta.tables['events'].columns['home_team_name'].create()
