from django.db import models
from django.urls import reverse

class InformationModel(models.Model):
	works_com = models.IntegerField(blank=True, null=True)
	years_of_ex = models.IntegerField(blank=True, null=True)
	total_clients = models.IntegerField(blank=True, null=True)

	def __str__ (self):
		return "name %s"%(self.works_com)
