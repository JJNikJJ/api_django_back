import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rental.models import Bike, User, Rental


@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    response = client.post(reverse('user_create'),
                           {'username': 'test', 'email': 'test@test.com', 'password': 'testtest123'})
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_bike_list():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpass123')
    client.force_authenticate(user=user)
    Bike.objects.create(name='Bike 1', description='Description 1', is_available=True)
    Bike.objects.create(name='Bike 2', description='Description 2', is_available=False)
    response = client.get(reverse('bike-list'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == 'Bike 1'
    assert response.data[1]['name'] == 'Bike 2'


@pytest.mark.django_db
def test_rent_bike():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpass123')
    client.force_authenticate(user=user)
    bike = Bike.objects.create(name='Bike 1', description='Description 1', is_available=True)
    response = client.post(reverse('rent_bike', kwargs={'pk': bike.id}))
    assert response.status_code == status.HTTP_200_OK
    bike.refresh_from_db()
    assert bike.is_available is False


@pytest.mark.django_db
def test_return_bike():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpass123')
    client.force_authenticate(user=user)
    bike = Bike.objects.create(name='Bike 1', description='Description 1', is_available=True)
    rental = Rental.objects.create(bike=bike, user=user)
    response = client.post(reverse('return_bike', kwargs={'pk': rental.id}))
    assert response.status_code == status.HTTP_200_OK
    rental.refresh_from_db()
    bike.refresh_from_db()
    assert rental.end_date is not None
    assert bike.is_available is True
