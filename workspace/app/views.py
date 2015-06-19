'''
Contains all of the site views. Basically a ToC.
This will be a lot of the meat of the app.
'''


from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"