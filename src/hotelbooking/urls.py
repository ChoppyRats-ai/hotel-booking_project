from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls