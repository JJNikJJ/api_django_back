from rest_framework import serializers
from .models import Bike, Rental, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User. Обрабатывает создание пользователя с зашифрованным паролем.
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Переопределение метода создания для зашифрования пароля.
        """
        user = User.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериализатор для получения JWT токена с добавлением имени пользователя.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class BikeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Bike.
    """

    class Meta:
        model = Bike
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Rental.
    """

    class Meta:
        model = Rental
        fields = '__all__'
