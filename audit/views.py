from django.shortcuts import render

# Create your views here.
from droneops.utils import RolePermission
permission_classes = [IsAuthenticated, RolePermission]
