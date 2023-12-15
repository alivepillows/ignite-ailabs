# views.py
from rest_framework.views import APIView, status
from .models import Course
from .serializer import CourseSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class CourseList(APIView):
    serializer = CourseSerializer
    pagination_class = CustomPaginator
    course = Course.objects.all()

    def get(self, request, format=None):
            course = Course.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(course, request)
            serializer = CourseSerializer(result_page, many=True)
            if not course.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({'detail': 'Data deleted'}, status=status.HTTP_404_NOT_FOUND)



