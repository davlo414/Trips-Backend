from rest_framework import permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .serializers import TripSerializer, TripTypeSerializer
from .models import Trip, TripType
from rest_framework.authtoken.models import Token

class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all().order_by('-start_date')
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

class TripTypeViewSet(viewsets.ModelViewSet):
    queryset = TripType.objects.all().order_by('name')
    serializer_class = TripTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserStatistics(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        token = request.headers['Authorization'].split(' ')[1]
        user = Token.objects.get(key=token).user
        user_trips = Trip.objects.filter(people=user)
        statistics = [
            {'label': 'Total number of trips', 'value': len(user_trips)},
            {'label': 'Miles hiked', 'value': user_trips.filter(trip_type__name='Hiking').aggregate(total_distance=Sum('distance'))['total_distance']},
            {'label': 'Miles biked', 'value': user_trips.filter(trip_type__name='Biking').aggregate(total_distance=Sum('distance'))['total_distance']},
        ]
        response = {
            "name": user.get_full_name(),
            "statistics": statistics
        }
        return Response(response)
