'''
Configuration file, called by __init__
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'bQ2wd9k2sTy907wk7u39R5oJzk1sbF7U'

OAUTH_CREDENTIALS = {
    'google': {
        'id': '159170913595-72jo5t2t9igm52ffk70e8ii321khnpi0',
        'secret': 'qd4LwMJ_GB1_gjkEfrG4MP0b'
    },
    'facebook': {
        'id': '1481279098860658',
        'secret': 'ca9501976b25b9223ebaa6febb25c56c'
    },
     'twitter': {
        'id': 'n/a',
        'secret': 'n/a'
    }
}