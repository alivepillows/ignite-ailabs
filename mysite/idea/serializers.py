from rest_framework import serializers
from .models import Ide
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ide
        fields = '__all__'