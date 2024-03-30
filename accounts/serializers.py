from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from trips.models import Trip

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source="user")
    shared_trips = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = '__all__'

    def get_shared_trips(self, obj):
        current_user = self.context.get('request').user
        return Trip.objects.filter(people__in=[current_user, obj.user]).count()