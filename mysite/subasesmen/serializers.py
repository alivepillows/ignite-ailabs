# serializers.py
from rest_framework import serializers
from .models import SubAsesmen

class SubAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAsesmen
        fields = '__all__'
