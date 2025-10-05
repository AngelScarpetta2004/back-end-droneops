from rest_framework import serializers
from .models import Telemetria, ReporteDano

class TelemetriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetria
        fields = '__all__'

class ReporteDanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteDano
        fields = '__all__'
