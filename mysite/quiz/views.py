# views.py
from rest_framework.views import APIView, status
from .models import Quiz, Jawaban, PivotJawaban
from .serializer import QuizSerializer, JawabanSerializer, PivotJawabanSerializer
from rest_framework.response import Response
from django.db.models import Sum

class QuizList(APIView):
    def get(self, request, format=None):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            quiz = Quiz.objects.get(pk=pk)
            serializer = QuizSerializer(quiz)
            return Response(serializer.data)
        except Quiz.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        quiz = Quiz.objects.get(pk=pk)
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        quiz = Quiz.objects.get(pk=pk)
        quiz.delete()
        return Response({'detail': 'Data deleted'})

class JawabanList(APIView):
    def get(self, request, format=None):
        jawaban = Jawaban.objects.all()
        serializer = JawabanSerializer(jawaban, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = JawabanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JawabanUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            jawaban = Jawaban.objects.get(pk=pk)
            serializer = JawabanSerializer(jawaban)
            return Response(serializer.data)
        except Jawaban.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        jawaban = Jawaban.objects.get(pk=pk)
        serializer = JawabanSerializer(jawaban, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        jawaban = Jawaban.objects.get(pk=pk)
        jawaban.delete()
        return Response({'detail': 'Data deleted'})

class PivotJawabanList(APIView):
    def get(self, request, format=None):
        pivotjawaban = PivotJawaban.objects.all()
        serializer = PivotJawabanSerializer(pivotjawaban, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PivotJawabanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PivotJawabanUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            pivotjawaban = PivotJawaban.objects.get(pk=pk)
            serializer = PivotJawabanSerializer(pivotjawaban)
            return Response(serializer.data)
        except PivotJawaban.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        pivotjawaban = PivotJawaban.objects.get(pk=pk)
        serializer = PivotJawabanSerializer(pivotjawaban, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pivotjawaban = PivotJawaban.objects.get(pk=pk)
        pivotjawaban.delete()
        return Response({'detail': 'Data deleted'})


class CalculateQuizValue(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming you send the quiz ID in the request data
        quiz_id = request.data.get('quiz_id', None)
        
        if not quiz_id:
            return Response({'error': 'Quiz ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

        # Your quiz calculation logic here
        # For example, you might want to calculate the value based on the answers
        # of the associated Jawaban instances.

        # Sample calculation logic:
        total_value = 0
        for pivot_jawaban in quiz.pivotjawaban_set.all():
            total_value += pivot_jawaban.total_nilai

        # Update the quiz value
        quiz.nilai = total_value
        quiz.save()

        return Response({'success': 'Quiz value calculated successfully'}, status=status.HTTP_200_OK)
