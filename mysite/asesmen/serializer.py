# serializers.py
from rest_framework import serializers
from .models import Asesmen, PivotAsesmen, SubAsesmen

class AsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesmen
        fields = '__all__'

class PivotAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PivotAsesmen
        fields = '__all__'

class SubAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAsesmen
        fields = '__all__'