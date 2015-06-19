'''
Identifies this folder as an application package (tells run.py where the app is)
'''


from flask import Flask

app = Flask(__name__)
from app import views