from rest_framework import status
from rest_framework import permissions
from rest_framework import views
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from .models import Ide
from rest_framework.decorators import api_view
from .serializers import IdeaSerializer
from rest_framework.response import Response

class IdeList(APIView):
    def get(self, request, format=None):
        ide = Ide.objects.all()
        serializer = IdeaSerializer(ide, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = IdeaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IdeDetail(APIView):
  def get(self, request, pk, format=None):
        try:
            ide = Ide.objects.get(pk=pk)
            serializer = IdeaSerializer(ide)
            return Response(serializer.data)
        except Ide.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
  def put(self, request, pk, format=None):
        ide = Ide.objects.get(pk=pk)
        serializer = IdeaSerializer(ide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, pk, format=None):
        try:
                ide = Ide.objects.all(pk=pk)
                ide.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Ide.DoesNotExist:
                    return Response({'detail': 'Ide not found'}, status=status.HTTP_404_NOT_FOUND)