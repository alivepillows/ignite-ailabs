from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import Ide
from .serializers import IdeSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .utils import Util
from rest_framework import response

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class IdeList(APIView):
    serializer_class = IdeSerializer
    pagination_class = CustomPaginator
    ide = Ide.objects.all()

    def get(self, request, format=None):
            ide = Ide.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(ide, request)
            serializer = IdeSerializer(result_page, many=True)
            if not ide.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        ide = serializer.data

        absurl = 'http://127.0.0.1:8000/register'
        email_body = 'Hi '+ide['name'] + \
            ' your idea is matter for Ignite! if you want to be telsiger, please use the link to register \n' + absurl
        data = {'email_body': email_body, 'to_email': ide['email'],
                'email_subject': 'Thanks for your idea!'}
        
        Util.send_email(data=data)
        return response.Response({'ide_data': ide}, status=status.HTTP_201_CREATED)

class IdeUpdateRetrieveDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            ide = Ide.objects.get(pk=pk)
            serializer = IdeSerializer(ide)
            return Response(serializer.data)
        except Ide.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        ide = Ide.objects.get(pk=pk)
        serializer = IdeSerializer(ide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        ide = Ide.objects.get(pk=pk)
        ide.delete()
        return Response({'detail': 'Data deleted'})
    


       
        
        

