from django.db import models
from repairs.models import ReporteArreglo

class LogCritico(models.Model):
    arreglo = models.ForeignKey(ReporteArreglo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50)  # "Alta", "Media", "Baja"
    timestamp = models.DateTimeField(auto_now_add=True)
