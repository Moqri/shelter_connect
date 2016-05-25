from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.

class Shelter(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,null=True)

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    date = models.DateTimeField(default=timezone.now)
    shelter=models.ForeignKey(Shelter,null=True)
    user=models.ForeignKey(User,null=True)