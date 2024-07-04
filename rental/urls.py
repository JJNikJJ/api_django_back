from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BikeViewSet, RentalViewSet

routers = DefaultRouter()
routers.register(r'bikes', BikeViewSet)
routers.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]