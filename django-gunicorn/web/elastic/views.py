from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch

# Create your views here.
def index(request):
    # Get a single document.
    es = Elasticsearch([{
        'host': 'elasticsearch',
        'port': 9200
    }])
    document = es.get(index='drupal', id=475262)
#    return render_template('story.html', story=document['_source'], document=document)
    content = document['_source']['headline'] + "<br />" + document['_source']['body']
    return HttpResponse(content)