from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from .models import Author
import json
import datetime
import sys

es = Elasticsearch([{'host':'elasticsearch', 'port':9200}])

def index(request):
	searchTerm = request.GET.get("q")
	esResponse = es.search(index='stories', q=searchTerm, sort="created:desc")['hits']['hits']
	return render(request, 'index.html',  {'stories': esResponse})

def story(request):
	storyId = request.path.rsplit('/', 1)[-1]
	esResponse = es.get(index='stories', id=storyId)['_source']
	publishDate = datetime.datetime.fromtimestamp(esResponse['created'])
	esResponse['publishDate'] = publishDate.strftime('%B %d, %Y %H:%M:%S')
	authorInfo = Author.objects.get(id=esResponse['author_uid'])

	return render(request, 'story.html', {'article': esResponse, 'author': authorInfo})

	