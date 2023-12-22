from rest_framework import serializers
from .models import Course, Rating, Benefit, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'
        extra_kwargs = {'password': {'write_only': True}}

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'bintang']

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ['id', 'deskripsi']

class CourseSerializer(serializers.ModelSerializer):
    rating = RatingSerializer()
    benefit = BenefitSerializer()
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
     


