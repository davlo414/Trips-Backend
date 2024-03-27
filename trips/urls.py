from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'trips', views.TripsViewSet)
router.register(r'trip-types', views.TripTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-statistics', views.UserStatistics.as_view())
]

urlpatterns += router.urls
