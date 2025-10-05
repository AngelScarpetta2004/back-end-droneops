from django.db import models
from users.models import User

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class TelemetryData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    drone_id = models.CharField(max_length=50)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class DroneEvent(models.Model):
    EVENT_LEVELS = (
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('critical', 'Critical'),
    )
    drone_id = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50)
    level = models.CharField(max_length=10, choices=EVENT_LEVELS)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
