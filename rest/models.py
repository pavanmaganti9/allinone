# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class employees(models.Model):
	
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	
	def __str__(self):
		return self.firstname