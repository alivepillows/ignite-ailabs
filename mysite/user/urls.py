from django.urls import path 
from .views import UserListCreate, UserRetrieveUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationView


urlpatterns = [
    path('user/', UserListCreate.as_view(), name= "create-user-list"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name= "user-details"),
    path('register/', UserRegistrationView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)