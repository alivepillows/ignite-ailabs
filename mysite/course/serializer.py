# serializers.py
from rest_framework import serializers
from .models import Course
from .utils import encrypt, decrypt

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'image', 'subcourse_id', 'level', 'user', 'rating']

    