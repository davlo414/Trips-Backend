from rest_framework import permissions, viewsets
from .serializers import ProfileSerializer
from .models import Profile
from django.db.models import Count
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('user__username')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]