from rest_framework import permissions, viewsets
from .serializers import ProfileSerializer
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('user__username')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]