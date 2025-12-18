from rest_framework import viewsets, permissions
from .models import MaintenanceRecord
from .serializers import MaintenanceRecordSerializer


class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
