# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

""" Initializes the database """
@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database')

""" Helper function to create database connection. The first time the function
    is called, it will create a database connection for the current context,
    and successive calls will return the already established connection. """
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

""" Helper function to close database at the end of the request. Flask provides
    us with the teardown_appcontext() decorator. It's executed every time
    the application context tears down. """
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
