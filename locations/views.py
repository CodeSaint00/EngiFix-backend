from rest_framework import viewsets, permissions
from .models import Location
from .serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]