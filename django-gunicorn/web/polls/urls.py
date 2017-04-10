from django.conf.urls import url

from . import views

# Set an application namespace for the URL configuration.
app_name = 'polls'

# Define URL patterns for this app.
urlpatterns = [
    # example: /polls/
    url(r'^$', views.index, name='index'),
    # example: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # example: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # example: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # example: /polls/views/
    url(r'^view/$', views.IndexView.as_view(), name='view_index'),
    # example: /polls/views/5/
    url(r'^view/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='view_detail'),
    # example: /polls/views/5/results
    url(r'^view/(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='view_results'),
    # example: /pools/views/5/vote
    url(r'^view/(?P<question_id>[0-9]+)/vote/$', views.vote, name='view_vote')
]