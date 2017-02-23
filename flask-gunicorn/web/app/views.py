from flask import render_template, flash, redirect
from elasticsearch import Elasticsearch
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    # Fake user.
    user = {'nickname': 'Miguel'}

    # Fake array of posts.
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/elasticsearch')
def elasticsearch():
    es = Elasticsearch([{
        'host': 'elasticsearch',
        'port': 9200
    }])
    indices = es.indices.get('drupal')

    return render_template('elasticsearch.html', debug=indices)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)