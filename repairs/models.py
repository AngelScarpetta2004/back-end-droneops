from django.db import models
from drones.models import DroneEvent

class RepairRecord(models.Model):
    drone_id = models.CharField(max_length=50)
    pieces_replaced = models.TextField()
    actions_taken = models.TextField()
    evidence = models.FileField(upload_to='repairs/')
    timestamp = models.DateTimeField(auto_now_add=True)
