# serializers.py
from rest_framework import serializers
from .models import Asesmen

class AsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesmen
        fields = '__all__'
