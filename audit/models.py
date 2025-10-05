from django.db import models
from users.models import User

class AuditLog(models.Model):
    ACTION_LEVELS = (
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('critical', 'Critical'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.TextField()
    level = models.CharField(max_length=10, choices=ACTION_LEVELS)
    timestamp = models.DateTimeField(auto_now_add=True)
