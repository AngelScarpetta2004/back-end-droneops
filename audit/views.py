from rest_framework import viewsets
from .models import LogCritico
from .serializers import LogCriticoSerializer
from droneops.utils import RolePermission

class LogCriticoViewSet(viewsets.ModelViewSet):
    queryset = LogCritico.objects.all()
    serializer_class = LogCriticoSerializer
    permission_classes = [RolePermission]
