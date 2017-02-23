from flask import Flask

# Instantiate a new variable by creating a Flask object.
app = Flask(__name__)

# Import configuration.
app.config.from_object('config')

# Import the views component from the app module (not the app variable).
from app import views