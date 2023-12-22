# serializers.py
from rest_framework import serializers
from .models import Asesmen, PivotAsesmen, SubAsesmen



class PivotAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PivotAsesmen
        fields = '__all__'
    
class SubAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAsesmen
        fields = '__all__'

class AsesmenSerializer(serializers.ModelSerializer):
    sub_asesmen = SubAsesmenSerializer(read_only=True)

    class Meta:
        model = Asesmen
        fields = '__all__'