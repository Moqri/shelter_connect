from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.

class Shelter(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,null=True)
    beds_total=models.IntegerField(default=0)
    beds_available=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Reservation(models.Model):
	name = models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.name