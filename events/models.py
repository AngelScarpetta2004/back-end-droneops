from django.db import models
from django.conf import settings

class Event(models.Model):
    EVENT_TYPES = [
        ('alarm', 'Alarma'),
        ('info', 'Información'),
        ('warning', 'Advertencia'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    drone_id = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.event_type})"
