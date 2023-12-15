from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import Benefit
from .serializer import BenefitSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class BenefitList(APIView):
    serializer = BenefitSerializer
    pagination_class = CustomPaginator
    benefit = Benefit.objects.all()

    def get(self, request, format=None):
            benefit = Benefit.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(benefit, request)
            serializer = BenefitSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
    def post(self, request, format=None):
            serializer = BenefitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BenefitUpdateRetrieveDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            benefit = Benefit.objects.get(pk=pk)
            serializer = BenefitSerializer(benefit)
            return Response(serializer.data)
        except Benefit.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        benefit = Benefit.objects.get(pk=pk)
        serializer = BenefitSerializer(benefit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        benefit = Benefit.objects.get(pk=pk)
        benefit.delete()
        return Response({'detail': 'Data deleted'})

