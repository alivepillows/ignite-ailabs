# views.py
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Asesmen, PivotAsesmen, SubAsesmen
from .serializer import AsesmenSerializer, SubAsesmenSerializer, PivotAsesmenSerializer 
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
    
  def post(self, request, format=None):
        serializer = PivotAsesmenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
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

     
class CalculateAsesmentValue(APIView):
    def get(self, request, asesmen_id):
        try:
            # Assuming asesmen_id is passed in the URL parameters
            asesmen = Asesmen.objects.get(id=asesmen_id)
            
            # Retrieve all related sub-asessments for the given assessment
            sub_asessments = SubAsesmen.objects.filter(pivotasessmen__asesmen=asesmen)

            # Calculate the total value of the assessment based on sub-asessments
            total_value = sum(sub_asessment.nilai for sub_asessment in sub_asessments)

            # Update the total value in the Asesmen model
            asesmen.total_value = total_value
            asesmen.save()

            return Response({'total_value': total_value}, status=status.HTTP_200_OK)

        except Asesmen.DoesNotExist:
            return Response({'error': 'Asesmen not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
