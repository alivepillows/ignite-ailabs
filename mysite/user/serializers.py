from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields ='__all__'
#         extra_kwargs = {'password': {'write_only': True}}
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'nama_depan', 'nama_belakang', 'image' , 'nomor', 'NIK' ,'Unit', 'role')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password']),
            nama_depan=validated_data['nama_depan'],
            nama_belakang=validated_data['nama_belakang'],
            # image=validated_data['image'],
            nomor=validated_data['nomor'],
            NIK=validated_data['NIK'],
            Unit=validated_data['Unit'],
            role=validated_data['role']
        )
    
        user.save()

        return User(**validated_data)