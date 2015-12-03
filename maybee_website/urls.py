#-*- coding: utf-8 -*-
from django.conf.urls import url
urlpatterns = patterns('maybee_website.views',
    url(r'^accueil$', 'home'),
) 
