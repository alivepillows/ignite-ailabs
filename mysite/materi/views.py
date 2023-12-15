from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import Materi
from .serializer import MateriSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class MateriList(APIView):
    serializer = MateriSerializer
    pagination_class = CustomPaginator
    materi = Materi.objects.all()

    def get(self, request, format=None):
            materi = Materi.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(materi, request)
            serializer = MateriSerializer(result_page, many=True)
            if not materi.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MateriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MateriUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            materi = Materi.objects.get(pk=pk)
            serializer = MateriSerializer(materi)
            return Response(serializer.data)
        except Materi.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        materi = Materi.objects.get(pk=pk)
        serializer = MateriSerializer(materi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        materi = Materi.objects.get(pk=pk)
        materi.delete()
        return Response({'detail': 'Data deleted'})

