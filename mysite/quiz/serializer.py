from rest_framework import serializers
from .models import Quiz, Jawaban, PivotJawaban

class JawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jawaban
        fields = '__all__'

class PivotJawabanSerializer(serializers.ModelSerializer):
    jawaban = JawabanSerializer()

    class Meta:
        model = PivotJawaban
        fields = '__all__'

    def create(self, validated_data):
        jawaban_data = validated_data.pop('jawaban')
        jawaban_instance = Jawaban.objects.create(**jawaban_data)
        pivot_jawaban_instance = PivotJawaban.objects.create(jawaban=jawaban_instance, **validated_data)
        return pivot_jawaban_instance

class QuizSerializer(serializers.ModelSerializer):
    jawaban = JawabanSerializer()
    pivot_jawabans = PivotJawabanSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def create(self, validated_data):
        jawaban_data = validated_data.pop('jawaban')
        jawaban_instance = Jawaban.objects.create(**jawaban_data)
        quiz_instance = Quiz.objects.create(jawaban=jawaban_instance, **validated_data)
        
        pivot_jawabans_data = validated_data.pop('pivot_jawabans', [])
        for pivot_jawaban_data in pivot_jawabans_data:
            PivotJawaban.objects.create(quiz=quiz_instance, **pivot_jawaban_data)

        return quiz_instance
