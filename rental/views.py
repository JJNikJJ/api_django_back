from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Bike, Rental
from .serializers import BikeSerializer, RentalSerializer, UserSerializer, MyTokenObtainPairSerializer
from .tasks import calculate_rental_cost


class BikeViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования объектов Bike.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RentalViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования объектов Rental.
    """
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def rent(self, request, pk=None):
        """
        Кастомное действие для аренды велосипеда.
        """
        bike = get_object_or_404(Bike, pk=pk)
        if not bike.is_available:
            return Response({'status': 'Bike is not available'}, status=400)
        rental = Rental.objects.create(bike=bike, user=request.user)
        bike.is_available = False
        bike.save()
        return Response({'status': 'Bike rented', 'rental_id': rental.id})

    @action(detail=True, methods=['post'])
    def return_bike(self, request, pk=None):
        """
        Кастомное действие для возврата арендованного велосипеда.
        """
        rental = self.get_object()
        rental.end_date = timezone.now()
        rental.save()
        rental.bike.is_available = True
        rental.bike.save()
        calculate_rental_cost.delay(rental.id)
        return Response({'status': 'Bike returned'})


class UserCreate(generics.CreateAPIView):
    """
    API представление для создания нового пользователя.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ObtainTokenPairView(TokenObtainPairView):
    """
    API представление для получения пары токенов (доступ и обновление).
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
