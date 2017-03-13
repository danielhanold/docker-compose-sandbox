from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.decorators.cache import cache_page
from django.urls import reverse
import json
import datetime
import sys

def environment(**options):
    env = Environment(**options)
    env.globals.update({
       'static': staticfiles_storage.url,
       'url': reverse,
    })
    return env

es = Elasticsearch([{'host':'elasticsearch', 'port':9200}])

def index(request):
	searchTerm = request.GET.get("q")
	esResponse = es.search(index='test-elastic', q=searchTerm, sort="created:desc")['hits']['hits']
	return render(request, 'index.html',  {'stories': esResponse})

def story(request):


	storyId = request.path.rsplit('/', 1)[-1]
	esResponse = es.get(index='test-elastic', id=storyId)['_source']
	publishDate = datetime.datetime.fromtimestamp(esResponse['created'])
	esResponse['publishDate'] = publishDate.strftime('%B %d, %Y %H:%M:%S')

	return render(request, 'story.html', {'article': esResponse})

def hello(request):
	return HttpResponse("HELLO SIMON")

