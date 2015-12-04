#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from django.template.context_processors import csrf
#from django.views.decorators.csrf import csrf_protect

from maybee_website.forms import ProfileForm, DataForm
from maybee_website.models import profil,Data


# Create your views here.
def home(request):
	return render(request, 'Home.html', locals())

def presentation(request):
	return render(request, 'presentation.html', locals())

def conseils(request):
	return render(request, 'conseils.html', locals())

def biblio(request):
	return render(request, 'biblio.html', locals())

def map(request):
	return render(request, 'map.html', locals())

def enfant_conte(request):
	return render(request, 'Enfant_conte.html', locals())

def profil(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			picked=form.cleaned_data.get('picked')
			#les lignes suivantes nécessitent de faire un routage vers une BDD
			#new_profil=profil(profil_nom=form.cleaned_data.get('your_name'),login=form.cleaned_data.get('login'),password=form.cleaned_data.get('password'))
			#new_profil.save()
			#print profil.objects.all()
	else:
		form = ProfileForm

	return render_to_response('apiculteurs.html', {'form':form },context_instance=RequestContext(request))


def apiculteurs(request):
	#c = {}
	#c.update(csrf(request))
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			donne=Data(adresse=form.cleaned_data.get('adresse'),nb_kilo_miel=form.cleaned_data.get('nb_kilo_miel'),
			nb_ruches=form.cleaned_data.get('nb_ruches'),type_miel=form.cleaned_data.get('type_miel'),
			evolution_population=form.cleaned_data.get('evolution_population'),facteurs=form.cleaned_data.get('facteurs'))# do something with your results
			donne.save()
			print Data.objects.all()
			print donne.verif()
			for donnee in Data.objects.filter(type_miel="lavande"):
				print(donnee.adresse, donnee.nb_ruches)
	else:
		form = DataForm
	
	return render(request,'apiculteur.html', locals())

