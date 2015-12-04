#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext


from maybee_website.forms import ProfileForm, DataForm
from maybee_website.models import profil,Data


# Create your views here.
def home(request):
	return render(request, 'Home.html', locals())

def profil(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			picked = form.cleaned_data.get('picked')
			print picked# do something with your results
	else:
		form = ProfileForm

	return render_to_response('apiculteurs.html', {'form':form },context_instance=RequestContext(request))



def apiculteurs(request):
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			picked = form.cleaned_data.get('picked')
			# do something with your results
	else:
		form = DataForm

	return render_to_response('apiculteurs.html', {'form':form },context_instance=RequestContext(request))

