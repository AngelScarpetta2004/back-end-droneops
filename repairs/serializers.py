from rest_framework import serializers
from .models import RepairRecord

class RepairRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairRecord
        fields = '__all__'

