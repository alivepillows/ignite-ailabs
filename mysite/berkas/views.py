# views.py
from rest_framework.views import APIView, status
from .models import Berkas
from .serializer import BerkasSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class BerkasList(APIView):
    serializer = BerkasSerializer
    pagination_class = CustomPaginator
    berkas = Berkas.objects.all()

    def get(self, request, format=None):
            berkas = Berkas.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(berkas, request)
            serializer = BerkasSerializer(result_page, many=True)
            if not berkas.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)
        
    def post(self, request, format=None):
            serializer = BerkasSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BerkasUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            berkas = Berkas.objects.get(pk=pk)
            serializer = BerkasSerializer(berkas)
            return Response(serializer.data)
        except Berkas.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        berkas = Berkas.objects.get(pk=pk)
        serializer = BerkasSerializer(berkas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        berkas = Berkas.objects.get(pk=pk)
        berkas.delete()
        return Response({'detail': 'Data deleted'}, status=status.HTTP_404_NOT_FOUND)



