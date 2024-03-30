from rest_framework import permissions, viewsets
from .serializers import ProfileSerializer
from .models import Profile
from django.db.models import Count
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Profile.objects.annotate(
            shared_trips_count=Count('user__trip', filter=Q(user__trip__people=current_user))
        ).exclude(user=current_user).order_by('-shared_trips_count')