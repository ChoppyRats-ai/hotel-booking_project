import pytest
from hotelbooking.models import Room

@pytest.fixture
def room():
    return Room.objects.create(
        description='Test Room',
        price_per_night=100.00
    )

@pytest.mark.django_db
class TestRoomAPI:
    def test_list_rooms(self, authenticated_client):
        response = authenticated_client.get('/api/v1/rooms/')
        assert response.status_code == 200

    def test_create_room(self, authenticated_client):
        data = {
            'description': 'New Room',
            'price_per_night': 150.00
        }
        response = authenticated_client.post('/api/v1/rooms/', data)
        assert response.status_code == 201
        assert response.data['description'] == 'New Room'

    def test_get_room_detail(self, authenticated_client, room):
        response = authenticated_client.get(f'/api/v1/rooms/{room.id}/')
        assert response.status_code == 200
        assert response.data['description'] == room.description
