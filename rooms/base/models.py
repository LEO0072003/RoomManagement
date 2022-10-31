from enum import unique
from random import choices
from unicodedata import name
from django.db import models

# Create your models here.

class Events(models.Model):
    """Model for events"""
    event_name = models.CharField(max_length=10)
    event_type = models.TextField(choices=[('public','public'),('private','private')], max_length=10)
    def __str__(self):
        return self.name

class Rooms(models.Model):
    """Model for rooms"""
    room_name = models.CharField(max_length=10, null=True, blank=True)
    capacity = models.IntegerField()
    event = models.OneToOneField(Events, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.name:
            return self.name
        else :
            return self.id

class Bookings(models.Model):
    """Model for Bookings"""
    room = models.OneToOneField(Rooms, unique=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.room)+""+str(self.room.event)
