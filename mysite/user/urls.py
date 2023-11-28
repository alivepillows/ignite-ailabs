from django.urls import path 
from .views import UserListCreate, UserRetrieveUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/', UserListCreate.as_view(), name= "create-user-list"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name= "user-details")
]