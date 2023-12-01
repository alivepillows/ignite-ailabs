# serializers.py
from rest_framework import serializers
from .models import PivotAsesmen

class PivotAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PivotAsesmen
        fields = '__all__'
