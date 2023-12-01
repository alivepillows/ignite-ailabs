# views.py
from rest_framework.views import APIView, status
from .models import SubAsesmen
from .serializers import SubAsesmenSerializer
from rest_framework.response import Response

class SubAsesmenList(APIView):
    def get(self, request, format=None):
        subasesmen = SubAsesmen.objects.all()
        serializer = SubAsesmenSerializer(subasesmen, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SubAsesmenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubAsesmenUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            subasesmen = SubAsesmen.objects.get(pk=pk)
            serializer = SubAsesmenSerializer(subasesmen)
            return Response(serializer.data)
        except SubAsesmen.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        subasesmen = SubAsesmen.objects.get(pk=pk)
        serializer = SubAsesmenSerializer(subasesmen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        subasesmen = SubAsesmen.objects.get(pk=pk)
        subasesmen.delete()
        return Response({'detail': 'Data deleted'})

