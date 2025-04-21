from typing import ClassVar

from rest_framework import serializers

from .models import Booking, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields: ClassVar[list[str]] = [
            'id', 'description', 'price_per_night', 'created_at'
        ]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields: ClassVar[list[str]] = [
            'id', 'room', 'date_start', 'date_end'
        ]
   
 
    