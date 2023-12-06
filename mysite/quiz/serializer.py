# serializers.py
from rest_framework import serializers
from .models import Quiz, Jawaban, PivotJawaban

from rest_framework import serializers

class JawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jawaban
        fields = '__all__'

class PivotJawabanSerializer(serializers.ModelSerializer):
    jawaban = JawabanSerializer()

    class Meta:
        model = PivotJawaban
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    jawaban = JawabanSerializer()
    pivot_jawabans = PivotJawabanSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'
