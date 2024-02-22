from django.db import models
from django.contrib.auth.models import User
    
class TripType(models.Model):
    '''A type of trip (hike, bike, etc.)'''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Trip(models.Model):
    '''An outdoors trip'''
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    distance = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    trip_type = models.ForeignKey(TripType, on_delete=models.PROTECT, null=True)
    date = models.DateField(blank=True, null=True)
    people = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return self.name