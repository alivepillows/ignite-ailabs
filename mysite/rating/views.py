from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import Rating
from .serializer import RatingSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class RatingList(APIView):
    serializer = RatingSerializer
    pagination_class = CustomPaginator
    rating = Rating.objects.all()

    def get(self, request, format=None):
            rating = Rating.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(rating, request)
            serializer = RatingSerializer(result_page, many=True)
            if not rating.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('course_id')
        data = request.data if isinstance(request.data, list) else [request.data]

        # Validate and create each rating
        for rating_data in data:
            rating_data['course'] = course_id
            serializer = self.get_serializer(data=rating_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RatingUpdate(APIView):
     def get(self, request, pk, format=None):
        try:
            rating = Rating.objects.get(pk=pk)
            serializer = RatingSerializer(rating)
            return Response(serializer.data)
        except Rating.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
     def put(self, request, pk, format=None):
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     def delete(self, request, pk, format=None):
        rating = Rating.objects.get(pk=pk)
        rating.delete()
        return Response({'detail': 'Data deleted'})