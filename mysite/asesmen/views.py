# views.py
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Asesmen, PivotAsesmen, SubAsesmen
from .serializer import AsesmenSerializer, SubAsesmenSerializer, PivotAsesmenSerializer 
from rest_framework.settings import api_settings 

class AsesmenListView(APIView):
    def get(self, request, format=None):
            asesmen = Asesmen.objects.all()
            serializer = AsesmenSerializer(asesmen, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
            serializer = AsesmenSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class AsesmenUpdateDeleteView(APIView):
     def get(self, request, pk, format=None):
        try:
            asesmen = Asesmen.objects.get(pk=pk)
            serializer = AsesmenSerializer(asesmen)
            return Response(serializer.data)
        except Asesmen.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
     def put(self, request, pk, format=None):
        asesmen = Asesmen.objects.get(pk=pk)
        serializer = AsesmenSerializer(asesmen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     def delete(self, request, pk, format=None):
        subasesmen = Asesmen.objects.get(pk=pk)
        subasesmen.delete()
        return Response({'detail': 'Data deleted'})

class PivotAsesmenListView(APIView):
  def get(self, request, format=None):
        pivotasesmen = PivotAsesmen.objects.all()
        serializer = PivotAsesmenSerializer(pivotasesmen, many=True)
        return Response(serializer.data)
    
  def post(self, request, *args, **kwargs):
        # Perform your calculation logic here
        sub_asesmen_id = request.data.get('sub_asesmen')
        sub_asesmen = SubAsesmen.objects.get(id=sub_asesmen_id)
        calculated_total_nilai = sub_asesmen.nilai * 2  # Adjust this calculation based on your logic

        # Create a new PivotAsesmen instance with the calculated value
        request.data['total_nilai'] = calculated_total_nilai
        serializer = PivotAsesmenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  
  def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}
  
class PivotAsesmenUpdateRetrieveDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            pivotasesmen = PivotAsesmen.objects.get(pk=pk)
            serializer = PivotAsesmenSerializer(pivotasesmen)
            return Response(serializer.data)
        except PivotAsesmen.DoesNotExist:
            return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, format=None):
        pivotasesmen = PivotAsesmen.objects.get(pk=pk)
        serializer = PivotAsesmenSerializer(pivotasesmen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pivotasesmen = PivotAsesmen.objects.get(pk=pk)
        pivotasesmen.delete()
        return Response({'detail': 'Data deleted'})

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

     
