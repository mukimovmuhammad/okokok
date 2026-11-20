from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Ride
from .serializers import BookingSerializer, RideSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def mukimov_create(self, serializer):
        serializer.save(driver=self.request.user)
        
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related('ride', 'passenger').all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def mukimov_create(self, serializer):
        serializer.save(passenger=self.request.user)
