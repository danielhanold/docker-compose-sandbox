from flask import Flask
from flask_admin import Admin
from flaskext.auth import Auth

# Instantiate a new variable by creating a Flask object.
app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
auth = Auth(app)

# Import configuration.
app.config.from_object('config')

# Import the views component from the app module (not the app variable).
from app import views