#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class profil(models.Model):
	profil_nom = models.CharField(max_length=255)
	login = models.CharField(max_length=50)
	password= models.CharField(max_length=20)
		
	def __str__(self):
		return self.profil_nom

class Data(models.Model):
	FACTEURS= (('a','Frelon asiatique'), ('b','Gel printanier'), ('c','printemps précoce'), ('d','pesticides'), ('e','OGM proches'))
	adresse = models.CharField(max_length=250)
	nb_kilo_miel = models.FloatField()
	nb_ruches = models.IntegerField()
	type_miel = models.CharField(max_length=50)
	evolution_population = models.FloatField()
	facteurs = models.CharField(max_length=50, choices=FACTEURS)

	def __str__(self):
				return self.adresse

	def verif(self):
		return self.type_miel,self.nb_ruches


		