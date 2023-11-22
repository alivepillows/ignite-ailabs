from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from .serializers import UserLoginSerializer

class UserListCreate(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()

        # Check if the queryset is empty
        if not queryset.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
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
    def get(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
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

    def delete(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'detail': 'Data deleted'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    

# class UserLoginView(TokenObtainPairView):
#     serializer_class = UserLoginSerializer

  
# class UserLoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(request, **serializer.validated_data)
#         if user is not None: 
#             login(request, user)
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'access_token': str(refresh.access_token),
#                 'refresh_token': str(refresh),
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)