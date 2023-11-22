from django.urls import path 
from .views import UserListCreate, UserRetrieveUpdateDelete

urlpatterns = [
    path('users', UserListCreate.as_view(), name= "create-user-list"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name= "user-details"),
    # path('login/', UserLoginView.as_view(), name='user-login'),
    # path('api/token', UserLoginView.as_view(), name='token_obtain_pair')
    # path('logout/', UserLogoutView.as_view(), name='user-logout')
]
