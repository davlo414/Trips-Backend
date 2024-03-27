from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source="user")
    
    class Meta:
        model = Profile
        fields = ['id', 'username', 'profile_picture']