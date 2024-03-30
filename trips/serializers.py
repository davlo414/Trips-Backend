from rest_framework import serializers
from .models import Trip, TripType


class TripTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripType
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    trip_type_id = serializers.IntegerField(write_only=True)
    trip_type = TripTypeSerializer(read_only=True)
    
    class Meta:
        model = Trip
        fields = '__all__'