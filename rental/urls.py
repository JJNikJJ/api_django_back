from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BikeViewSet, RentalViewSet, UserCreate, ObtainTokenPairView

routers = DefaultRouter()
routers.register(r'bikes', BikeViewSet)
routers.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('register/', UserCreate.as_view(), name='user_create'),
    path('token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('bikes/<int:pk>/rent/', RentalViewSet.as_view({'post': 'rent'}), name='rent_bike'),
    path('rentals/<int:pk>/return/', RentalViewSet.as_view({'post': 'return_bike'}), name='return_bike'),
]
