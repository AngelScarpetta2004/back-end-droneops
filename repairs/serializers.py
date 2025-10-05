from rest_framework import serializers
from .models import ReporteArreglo

class ReporteArregloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteArreglo
        fields = '__all__'
