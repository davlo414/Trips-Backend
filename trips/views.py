from .models import Trip
from rest_framework import permissions, viewsets

from .serializers import TripSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all().order_by('-date')
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]