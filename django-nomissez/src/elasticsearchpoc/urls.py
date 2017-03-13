from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name='index'),
			   url(r'^story/', views.story, name='elastic_story'),
			   url(r'^hello/', views.hello, name='elastic_hello'),]

