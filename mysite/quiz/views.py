# views.py
from rest_framework.views import APIView, status
from .models import Quiz
from .serializer import QuizSerializer
from rest_framework.response import Response

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


