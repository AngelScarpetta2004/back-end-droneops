from django.db import models

class Telemetria(models.Model):
    numero_serie = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    dias_espacio = models.IntegerField()
    carga = models.CharField(max_length=50)
    estado_comunicacion = models.CharField(max_length=50)
    version_software = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class ReporteDano(models.Model):
    TIPO_DANO = (
        ("Letal", "Letal"),
        ("Grave", "Grave"),
        ("Moderado", "Moderado"),
        ("Minimo", "Mínimo"),
    )
    CONDICION = (
        ("Dañado", "Dañado"),
        ("Reparado", "Reparado"),
    )
    telemetria = models.ForeignKey(Telemetria, on_delete=models.CASCADE, related_name='reportes')
    tipo = models.CharField(max_length=50, choices=TIPO_DANO)
    gravedad = models.CharField(max_length=10, choices=TIPO_DANO)
    condicion = models.CharField(max_length=10, choices=CONDICION)
    foto_url = models.URLField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100)
    id_unico = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
