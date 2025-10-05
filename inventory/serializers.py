from rest_framework import serializers
from .models import Part, Inventory, BOM

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class BOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM
        fields = '__all__'
