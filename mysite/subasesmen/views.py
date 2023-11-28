from rest_framework import status
from rest_framework import permissions
from rest_framework import views
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from .models import User, Ide, SubAsesmen, Asesmen, PivotAsesmen
from rest_framework.decorators import api_view
from .serializers import SubAsesmenSerializer, AsesmenSerializer, PivotAsesmenSerializer
from rest_framework.response import Response

class SubAsesmenListCreateView(APIView):
     def get(self, request, format=None):
        queryset = SubAsesmen.objects.all()

        # Check if the queryset is empty
        if not queryset.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubAsesmenSerializer(queryset, many=True)
        return Response(serializer.data)
     
     def post(self, request, format=None):
       serializer = SubAsesmenSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AsesmenList(APIView):
    def get(self, request):
        asesmen = Asesmen.objects.all()
        serializer = AsesmenSerializer(asesmen, many=True)
        if not asesmen.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubAsesmenSerializer(asesmen, many=True)
        return Response(serializer.data)
     
    
    def post(self, request, format=None):
        serializer = AsesmenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)