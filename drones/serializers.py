from rest_framework import serializers
from .models import Sensor, TelemetryData, DroneEvent

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class TelemetryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemetryData
        fields = '__all__'

class DroneEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneEvent
        fields = '__all__'
