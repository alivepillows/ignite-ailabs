# serializers.py
from rest_framework import serializers
from .models import Berkas

class BerkasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berkas
        fields = '__all__'


    