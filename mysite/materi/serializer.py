# serializers.py
from rest_framework import serializers
from .models import Materi

class MateriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materi
        fields = '__all__'
