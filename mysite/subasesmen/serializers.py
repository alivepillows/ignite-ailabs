from rest_framework import serializers
from .models import SubAsesmen, PivotAsesmen, Asesmen
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class SubAsesmenSerializer(serializers.Serializer):
    class Meta:
        model = SubAsesmen
        fields = '__all__'

class PivotAsesmenSerializer(serializers.Serializer):
    asesmen = SubAsesmenSerializer
    class Meta:
        model = PivotAsesmen
        fields= '__all__'

class AsesmenSerializer(serializers.Serializer):
    asesmen= serializers.SerializerMethodField
    class Meta:
        model= Asesmen
        fields = '__all__'
        depth = 1
     
    def get_asesmen(self, obj):
        query_set = PivotAsesmen.objects.filter(product=obj)
        return[PivotAsesmenSerializer(item).data for item in query_set]