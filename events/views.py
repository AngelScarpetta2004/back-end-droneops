from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from droneops.utils import RolePermission

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [RolePermission]
