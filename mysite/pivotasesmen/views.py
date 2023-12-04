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
  
class PivotAsesmenUpdateRetrieveDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            pivotasesmen = PivotAsesmen.objects.get(pk=pk)
            serializer = PivotAsesmenSerializer(pivotasesmen)
            return Response(serializer.data)
        except PivotAsesmen.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        pivotasesmen = PivotAsesmen.objects.get(pk=pk)
        serializer = PivotAsesmenSerializer(pivotasesmen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pivotasesmen = PivotAsesmen.objects.get(pk=pk)
        pivotasesmen.delete()
        return Response({'detail': 'Data deleted'})
