from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import Ide
from .serializers import IdeSerializer
from rest_framework.response import Response

class IdeList(APIView):
    def get(self, request, format=None):
        ide = Ide.objects.all()
        if not ide.exists(): 
            return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IdeSerializer(ide, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = IdeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IdeUpdateRetrieveDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            ide = Ide.objects.get(pk=pk)
            serializer = IdeSerializer(ide)
            return Response(serializer.data)
        except Ide.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        ide = Ide.objects.get(pk=pk)
        serializer = IdeSerializer(ide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        ide = Ide.objects.get(pk=pk)
        ide.delete()
        return Response({'detail': 'Data deleted'})

