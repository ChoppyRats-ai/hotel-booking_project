from typing import ClassVar

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q


class Room(models.Model):
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ClassVar[list[str]] = ['-created_at']

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    date_start = models.DateField()
    date_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ClassVar[list[str]] = ['date_start']

    def clean(self):
        if self.date_start and self.date_end:
            if self.date_start > self.date_end:
                raise ValidationError('Дата начала не может быть позже даты окончания')
            
            overlapping_bookings = Booking.objects.filter(
                room=self.room
            ).filter(
                Q(date_start__lte=self.date_end) & Q(date_end__gte=self.date_start)
            )
            
            if self.pk:
                overlapping_bookings = overlapping_bookings.exclude(pk=self.pk)
            
            if overlapping_bookings.exists():
                raise ValidationError('Эти даты уже забронированы')

