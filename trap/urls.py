from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, RideViewSet

router = DefaultRouter()
router.register('rides', RideViewSet)
router.register('bookings', BookingViewSet)
urlpatterns = router.urls
