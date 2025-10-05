from rest_framework import serializers
from .models import LogCritico

class LogCriticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCritico
        fields = '__all__'
