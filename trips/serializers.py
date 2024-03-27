from rest_framework import serializers
from .models import Trip, TripType

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class TripTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripType
        fields = '__all__'