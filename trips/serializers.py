from .models import Trip
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['name', 'lat', 'lon', 'distance', 'trip_type', 'date', 'people']