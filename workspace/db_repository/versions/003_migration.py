#Added events and relationships

from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
association = Table('association', post_meta,
    Column('user_id', Integer),
    Column('event_id', Integer),
)

events = Table('events', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_name', String(length=120)),
    Column('venue_id', String(length=120)),
    Column('game_id', String(length=120)),
    Column('event_score', Integer),
    Column('creator_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['association'].create()
    post_meta.tables['events'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['association'].drop()
    post_meta.tables['events'].drop()
