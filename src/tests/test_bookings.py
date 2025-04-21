import pytest
from datetime import date
from hotelbooking.models import Room, Booking

@pytest.fixture
def room():
    return Room.objects.create(
        description='Test Room',
        price_per_night=100.00
    )

@pytest.fixture
def booking(room):
    return Booking.objects.create(
        room=room,
        date_start=date(2024, 3, 1),
        date_end=date(2024, 3, 5)
    )

@pytest.mark.django_db
class TestBookingAPI:
    def test_list_bookings(self, authenticated_client):
        response = authenticated_client.get('/api/v1/bookings/')
        assert response.status_code == 200

    def test_create_booking(self, authenticated_client, room):
        data = {
            'room': room.id,
            'date_start': '2024-03-10',
            'date_end': '2024-03-15'
        }
        response = authenticated_client.post('/api/v1/bookings/', data)
        assert response.status_code == 201

    def test_get_booking_detail(self, authenticated_client, booking):
        response = authenticated_client.get(f'/api/v1/bookings/{booking.id}/')
        assert response.status_code == 200

    def test_cannot_book_overlapping_dates(self, authenticated_client, room, booking):
        data = {
            'room': room.id,
            'date_start': '2024-03-03',
            'date_end': '2024-03-07'
        }
        response = authenticated_client.post('/api/v1/bookings/', data)
        assert response.status_code == 400  # should fail due to date overlap
