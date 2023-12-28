# serializers.py
from rest_framework import serializers, exceptions
from .models import Asesmen, PivotAsesmen, SubAsesmen

class PivotAsesmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PivotAsesmen
        fields =[
            "id",
            "asesmen",
            "sub_asesmen",
            "total_nilai"
        ] 
    
class SubAsesmenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    class Meta:
        model = SubAsesmen
        fields = [
            "id",
            "pertanyaan",
            "nilai"
            ]

class AsesmenSerializer(serializers.ModelSerializer):
    sub_asesmen = SubAsesmenSerializer(many=True, read_only=True)
    class Meta:
        model = Asesmen
        fields = [
            "id",
            "tgl_mulai",
            "tgl_akhir",
            "time_expired",
            "image",
            "sub_asesmen",
            "title"
        ]

def create(self, validated_data):
    sub_asesmen_data = validated_data.pop('sub_asesmen')

    try:
        asesmen = Asesmen.objects.create(**validated_data)
    except exceptions.ValidationError as e:
        print("Validation error:", e.detail)
        raise

    for sub_asesmen_item in sub_asesmen_data:
        SubAsesmen.objects.create(asesmen=asesmen, **sub_asesmen_item)

    return asesmen