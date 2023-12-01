# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PivotAsesmen
from .serializer import PivotAsesmenSerializer

class PivotAsesmenListView(APIView):
  def get(self, request, format=None):
        pivotasesmen = PivotAsesmen.objects.all()
        serializer = PivotAsesmenSerializer(pivotasesmen, many=True)
        return Response(serializer.data)
    
  def post(self, request, format=None):
        serializer = PivotAsesmenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  