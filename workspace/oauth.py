from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session
from config import OAUTH_CREDENTIALS

import json, urllib2

class GoogleSignIn(object):
    def __init__(self):
        credentials = OAUTH_CREDENTIALS['google']
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']
        self.consumer_redirect = credentials['redirect']
        googleinfo = urllib2.urlopen('https://accounts.google.com/.well-known/openid-configuration')
        google_params = json.load(googleinfo)
        self.service = OAuth2Service(
            name='google',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url=google_params.get('authorization_endpoint'),
            access_token_url=google_params.get('token_endpoint'),
            base_url=google_params.get('userinfo_endpoint')
        )
        
    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email',
            response_type='code',
            redirect_uri=self.consumer_redirect)
        )

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.consumer_redirect }, 
                  
            decoder=json.loads
        )
        print 'DEBUG_1.1'
        print 'oauth_session'
        print oauth_session
        print 'oauth_session'
        me = oauth_session.get('').json()
        print 'me'
        print me
        print 'me'
        print 'DEBUG_1.2'
        name = me.get('name')
        email = me.get('email')
        return name, email