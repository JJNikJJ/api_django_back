import pytest
from rental.models import Bike, User


@pytest.mark.django_db
def test_bike_creation():
    bike = Bike.objects.create(name='Test Bike', description='Test Description', is_available=True)
    assert bike.name == 'Test Bike'
    assert bike.description == 'Test Description'
    assert bike.is_available is True


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username='testuser', email='test@test.com', password='testpassword')
    assert user.username == 'testuser'
    assert user.email == 'test@test.com'
    assert user.check_password('testpassword') is True
