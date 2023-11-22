from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'password',
            'image',
            'phone_number',
            'nik_ts',
            'unit_bisnis',
            'point',
            'course',
            'role',
            'username'
        )
 
