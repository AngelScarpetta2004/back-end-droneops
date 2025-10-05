from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)  # Ej. 'Herramienta', 'Pieza Básica', 'Pieza Avanzada'
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    hash_value = models.CharField(max_length=64, blank=True)  # SHA-256 opcional
