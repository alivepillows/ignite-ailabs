from rest_framework import serializers
from .models import User,Ide

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'
        extra_kwargs = {'password': {'write_only': True}}

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ide
        fields = '__all__'