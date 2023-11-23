from django.urls import path 
from .views import UserListCreate, UserRetrieveUpdateDelete, IdeList, IdeDetail

urlpatterns = [
    path('users', UserListCreate.as_view(), name= "create-user-list"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name= "user-details"),
    path('idea', IdeList.as_view(), name='create-ide-list' ),
    path('ide/<int:pk>', IdeDetail.as_view(), name='ide-detail')
]
