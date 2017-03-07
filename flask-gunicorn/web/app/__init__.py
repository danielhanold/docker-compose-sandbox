from flask import Flask, session, flash
from flask_admin import Admin
from flaskext.auth import Auth
from flask_assets import Environment, Bundle

# Instantiate a new variable by creating a Flask object.
app = Flask(__name__)

# Initialize packes.
admin = Admin(app, name='microblog', template_mode='bootstrap3')
auth = Auth(app)
assets = Environment(app)

# Import configuration.
app.config.from_object('config')

# Import the views component from the app module (not the app variable).
from app import views