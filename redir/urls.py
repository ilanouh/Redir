# -*- coding: utf-8 -*-
"""
Urls for redir
"""
from django.conf.urls import patterns, url

from project.redir import views

urlpatterns = patterns('views',
    url(r'^$', views.HomeView.as_view(), name='home-view'),
    url(r'^(?P<slug>[-\w]+)/$', views.RedirView.as_view(), name='url-view'),
)
