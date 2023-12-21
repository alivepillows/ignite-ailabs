# serializers.py

from rest_framework import serializers
from .models import Course, SubCourse, Rating, Benefit, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class SubCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCourse
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    #usedr = UserSerializer()
    rating = RatingSerializer(source="id", read_only=True)
    benefit= BenefitSerializer(source="id", read_only=True)
    subcourse = SubCourseSerializer(source="id", read_only=True)

    class Meta:
        model = Course
        fields = ['id','image','user','subcourse', 'rating', 'level', 'benefit', 'subcourse']

    