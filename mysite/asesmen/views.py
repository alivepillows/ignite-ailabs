# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Asesmen
from .serializer import AsesmenSerializer

class AsesmenListView(APIView):
  def get(self, request, format=None):
        asesmen = Asesmen.objects.all()
        serializer = AsesmenSerializer(asesmen, many=True)
        return Response(serializer.data)
    
  def post(self, request, format=None):
        serializer = AsesmenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class AsesmenUpdateDeleteView(APIView):
     def get(self, request, pk, format=None):
        try:
            asesmen = Asesmen.objects.get(pk=pk)
            serializer = AsesmenSerializer(asesmen)
            return Response(serializer.data)
        except Asesmen.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
     def put(self, request, pk, format=None):
        asesmen = Asesmen.objects.get(pk=pk)
        serializer = AsesmenSerializer(asesmen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     def delete(self, request, pk, format=None):
        subasesmen = Asesmen.objects.get(pk=pk)
        subasesmen.delete()
        return Response({'detail': 'Data deleted'})
