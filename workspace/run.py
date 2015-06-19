'''
Starts the application
Use the following command:
python run.py

Set up ip and ports here.
Set up debug here.
'''

import os
from app import app
app.run(os.getenv('IP'), int(os.getenv('PORT')),debug=True)