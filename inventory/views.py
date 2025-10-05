from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from droneops.utils import RolePermission

class HerramientaViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [RolePermission]
