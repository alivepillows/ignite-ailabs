# serializers.py
from rest_framework import serializers
from .models import SubCourse

class SubCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCourse
        fields = '__all__'
