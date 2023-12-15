from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import SubCourse
from .serializer import SubCourseSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class SubcourseList(APIView):
    serializer = SubCourseSerializer
    pagination_class = CustomPaginator
    subcourse = SubCourse.objects.all()

    def get(self, request, format=None):
            subcourse = SubCourse.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(subcourse, request)
            serializer = SubCourseSerializer(result_page, many=True)
            if not subcourse.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SubCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubcourseUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            subcourses = SubCourse.objects.get(pk=pk)
            serializer = SubCourseSerializer(subcourses)
            return Response(serializer.data)
        except SubCourse.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        subcourses = SubCourse.objects.get(pk=pk)
        serializer = SubCourseSerializer(subcourses, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        subcourses = SubCourse.objects.get(pk=pk)
        subcourses.delete()
        return Response({'detail': 'Data deleted'})

