from rest_framework import (status, permissions, views, generics)
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserRegisterSerializer

class CustomPaginator(PageNumberPagination):
    page_size= 5
    page_query_param="page"
    page_size_query_param="page_size"

class UserListCreate(APIView):
    serializer = UserSerializer
    pagination_class = CustomPaginator
    user = User.objects.all()

    def get(self, request, format=None):
            user = User.objects.all()
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(user, request)
            serializer = UserSerializer(result_page, many=True)
            if not user.exists():
               return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving the user
            validated_data = serializer.validated_data
            validated_data['password'] = make_password(validated_data['password'])
            profile_image = request.data.get('profile_image')
            if profile_image:
                validated_data['profile_image'] = profile_image
            serializer.save()
            return Response({'detail': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateDelete(APIView):
    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                # Hash the password before saving the user
                validated_data = serializer.validated_data
                validated_data['password'] = make_password(validated_data['password'])
                serializer.save()
                return Response({'detail': 'Data updated'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'detail': 'Data deleted'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user'] = { "username" : user.username , "email" : user.email }

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer