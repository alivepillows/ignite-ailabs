from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import SubCourse
from .serializer import SubCourseSerializer
from rest_framework.response import Response

class MateriList(APIView):
    def get(self, request, format=None):
        materi = SubCourse.objects.all()
        if not materi.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubCourseSerializer(materi, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SubCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MateriUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            materi = SubCourse.objects.get(pk=pk)
            serializer = SubCourseSerializer(materi)
            return Response(serializer.data)
        except SubCourse.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        subasesmen = SubCourse.objects.get(pk=pk)
        serializer = SubCourseSerializer(subasesmen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        subasesmen = SubCourse.objects.get(pk=pk)
        subasesmen.delete()
        return Response({'detail': 'Data deleted'})

