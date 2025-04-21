from rest_framework import viewsets
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

from .models import Booking, Room  # только нужные модели
from .serializers import BookingSerializer, RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        sort_by = self.request.query_params.get('sort_by', None)
        order = self.request.query_params.get('order', 'asc')
        
        if sort_by == 'price':
            order_field = 'price_per_night' if order == 'asc' else '-price_per_night'
            queryset = queryset.order_by(order_field)
        elif sort_by == 'date':
            order_field = 'created_at' if order == 'asc' else '-created_at'
            queryset = queryset.order_by(order_field)
            
        return queryset

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            booking = serializer.save()
            booking.clean()  # Вызываем проверку
            booking.save()
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)