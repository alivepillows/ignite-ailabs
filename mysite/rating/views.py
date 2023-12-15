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
    
    def post(self, request, format=None):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)