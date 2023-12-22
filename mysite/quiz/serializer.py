from rest_framework import serializers
from .models import Quiz, Jawaban, PivotJawaban

class JawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jawaban
        fields = '__all__'

class PivotJawabanSerializer(serializers.ModelSerializer):

    class Meta:
        model = PivotJawaban
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'

