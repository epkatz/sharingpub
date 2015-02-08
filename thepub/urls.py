from django.conf.urls import patterns, url
from thepub import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^share/$', views.share),
)