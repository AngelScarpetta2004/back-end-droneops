from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Inventory(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)

class BOM(models.Model):
    drone_model = models.CharField(max_length=50)
    parts = models.ManyToManyField(Part)

