# serializers.py
from rest_framework import serializers
from .models import Ide

class IdeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ide
        fields = '__all__'
