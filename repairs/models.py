from django.db import models
from drones.models import Telemetria

class ReporteArreglo(models.Model):
    ESTADO = (
        ("En revisión", "En revisión"),
        ("En proceso", "En proceso"),
        ("Desconocido", "Desconocido"),
        ("Completado", "Completado"),
    )
    telemetria = models.ForeignKey(Telemetria, on_delete=models.CASCADE)
    material_usado = models.JSONField(default=list)  # [{"nombre": "...", "cantidad": 1}]
    estado = models.CharField(max_length=20, choices=ESTADO)
    foto_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100)
    metricas_exito = models.JSONField(default=dict)  # {"eficiencia": "50%->90%"}
    hash_seguridad = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
