from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ReporteArreglo
from .serializers import ReporteArregloSerializer
from droneops.utils import RolePermission

class ReporteArregloViewSet(viewsets.ModelViewSet):
    queryset = ReporteArreglo.objects.all()
    serializer_class = ReporteArregloSerializer
    permission_classes = [RolePermission]
