from rest_framework import viewsets
from .models import Telemetria, ReporteDano
from .serializers import TelemetriaSerializer, ReporteDanoSerializer
from droneops.utils import RolePermission

class TelemetriaViewSet(viewsets.ModelViewSet):
    queryset = Telemetria.objects.all()
    serializer_class = TelemetriaSerializer
    permission_classes = [RolePermission]

class ReporteDanoViewSet(viewsets.ModelViewSet):
    queryset = ReporteDano.objects.all()
    serializer_class = ReporteDanoSerializer
    permission_classes = [RolePermission]
