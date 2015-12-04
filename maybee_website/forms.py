#-*- coding: utf-8 -*-
from django import forms

class ProfileForm(forms.Form):
	your_name = forms.CharField(label='Nom', max_length=100)
	login = forms.CharField(label='Login', max_length=50)
	password = forms.CharField(label='mot de passe', max_length=50)


class DataForm(forms.Form):
	FACTEURS = (('a','Frelon asiatique'), ('b','Gel printanier'), ('c','printemps précoce'), ('d','pesticides'), ('e','OGM proches'),)
	adresse = forms.CharField(label="Adresse de l'emplacement des ruches")
	nb_kilo_miel = forms.FloatField(label='Nombre de kilos de miel récoltés')
	nb_ruches = forms.IntegerField(label='Nombre de ruches actives')
	type_miel = forms.CharField(label='Type de miel récolté', max_length=50)
	evolution_population = forms.FloatField(label='Evolution de la population (en pourcentage de perte ou de croissance')
	facteurs = forms.MultipleChoiceField(label="Facteurs potentiels en cas de pertes d'abeilles",choices=FACTEURS, widget=forms.CheckboxSelectMultiple())
