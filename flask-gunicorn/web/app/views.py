from flask import render_template, request
from elasticsearch import Elasticsearch
from app import app
from datetime import datetime
from .forms import LoginForm
import logging

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

    # See if a search was already executed.
    search_value = request.args.get('q')
    if search_value == None:
        app.logger.error('No search value found')
        result = es.search(index='drupal', sort='nid:desc')
        search_executed = False
        list_headline = "Most Recent Stories"
    else:
        app.logger.error('Found a search value, which is %s', str(search_value))
        result = es.search(index='drupal', q=search_value, sort='nid:desc')
        list_headline = '%s results for the term "%s" - Showing you the top ten:' % (result['hits']['total'], search_value)
        search_executed = True

    # Assign the hits to a variable.
    if result['hits']['total'] > 0:
        hits = result['hits']['hits']
    else:
        hits = []

    return render_template('elasticsearch.html', debug=result, hits=hits, search_executed=search_executed, list_headline=list_headline)

@app.route('/story/<id>')
def story_id(id):
    es = Elasticsearch([{
        'host': 'elasticsearch',
        'port': 9200
    }])

    # Get a single document.
    document = es.get(index='drupal', id=id)

    return render_template('story.html', story=document['_source'], document=document)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

# Add custom filter for better time display.
# @see http://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date-in-python
# @see https://coderwall.com/p/-uuawg/how-do-i-convert-a-unix-timestamp-to-human-readable-format-in-python
def datetimeformat(value, format='%a, %B %-d, %Y'):
    return datetime.fromtimestamp(value).strftime(format)
app.jinja_env.filters['datetimeformat'] = datetimeformat