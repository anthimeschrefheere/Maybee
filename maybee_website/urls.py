#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
urlpatterns = patterns('maybee_website.views',
    url(r'^accueil$', 'home'),url(r'^apiculteurs$', 'apiculteurs'),url(r'^profil$','profil'),url(r'^services1$','presentation'),url(r'^services2$','conseils'),url(r'^biblio$','biblio')
) 
