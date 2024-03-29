from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^$', views.HomeView.as_view(), name='index'),
]